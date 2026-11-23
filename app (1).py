
import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(
    page_title="CyberSentinel AI",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ CyberSentinel AI")
st.subheader("Intelligent Network Threat Detection")

st.write(
    "AI-powered network traffic classification "
    "using Machine Learning."
)

# Load trained model
MODEL_PATH = "models/cybersentinel_model.pkl"

if not os.path.exists(MODEL_PATH):
    st.error("Trained model file not found.")
    st.stop()

saved = joblib.load(MODEL_PATH)
model = saved["model"]
features = saved["features"]

# Network dataset feature names
columns = [
    "duration", "protocol_type", "service", "flag",
    "src_bytes", "dst_bytes", "land", "wrong_fragment",
    "urgent", "hot", "num_failed_logins", "logged_in",
    "num_compromised", "root_shell", "su_attempted",
    "num_root", "num_file_creations", "num_shells",
    "num_access_files", "num_outbound_cmds",
    "is_host_login", "is_guest_login", "count",
    "srv_count", "serror_rate", "srv_serror_rate",
    "rerror_rate", "srv_rerror_rate", "same_srv_rate",
    "diff_srv_rate", "srv_diff_host_rate",
    "dst_host_count", "dst_host_srv_count",
    "dst_host_same_srv_rate", "dst_host_diff_srv_rate",
    "dst_host_same_src_port_rate",
    "dst_host_srv_diff_host_rate",
    "dst_host_serror_rate", "dst_host_srv_serror_rate",
    "dst_host_rerror_rate", "dst_host_srv_rerror_rate"
]

st.divider()

st.header("Upload Network Traffic Data")

uploaded = st.file_uploader(
    "Upload a headerless NSL-KDD CSV file",
    type=["csv"]
)

if uploaded is not None:

    try:
        data = pd.read_csv(uploaded, header=None)

        # Remove label and difficulty columns
        if data.shape[1] == 43:
            data = data.iloc[:, :41]

        if data.shape[1] != 41:
            st.error(
                "Please upload a CSV with 41 network features "
                "or 43 columns including label and difficulty."
            )
            st.stop()

        data.columns = columns

        st.success("Network traffic data loaded!")

        # Convert categorical features
        processed = pd.get_dummies(
            data,
            columns=["protocol_type", "service", "flag"]
        )

        # Match training feature structure
        processed = processed.reindex(
            columns=features,
            fill_value=0
        )

        predictions = model.predict(processed)

        results = data.copy()

        results["Prediction"] = [
            "Normal" if value == 0 else "Suspicious"
            for value in predictions
        ]

        if hasattr(model, "predict_proba"):
            confidence = model.predict_proba(processed).max(axis=1)
            results["Model Confidence"] = (
                confidence * 100
            ).round(2)

        normal = int((predictions == 0).sum())
        suspicious = int((predictions == 1).sum())

        st.divider()
        st.header("Threat Detection Results")

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Records", len(results))
        col2.metric("Normal Traffic", normal)
        col3.metric("Suspicious Traffic", suspicious)

        st.subheader("Traffic Classification")
        st.bar_chart(
            pd.DataFrame({
                "Records": [normal, suspicious]
            }, index=["Normal", "Suspicious"])
        )

        st.subheader("Prediction Details")
        st.dataframe(results, use_container_width=True)

        csv = results.to_csv(index=False).encode("utf-8")

        st.download_button(
            "Download Prediction Report",
            data=csv,
            file_name="cybersentinel_report.csv",
            mime="text/csv"
        )

    except Exception as error:
        st.error(f"Could not process the file: {error}")

else:
    st.info("Upload an NSL-KDD CSV file to begin analysis.")

st.divider()
st.caption(
    "CyberSentinel AI | Educational ML-based intrusion detection. "
    "Predictions require independent security verification."
)
