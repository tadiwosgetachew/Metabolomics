import streamlit as st
from PIL import Image
import os
import json
import plotly.graph_objects as go
import re


st.set_page_config(page_title="Metabolomics Dashboard", layout="wide")    # App config
st.title("Metabolomics Results Dashboard")
st.markdown("""
This dashboard presents the results of a **targeted LC-MS metabolomics analysis** focused on **colorectal cancer**. It includes key visualizations from Principal Component Analysis (PCA), Partial Least Squares Discriminant Analysis (PLS-DA), Metabolite Set Enrichment Analysis (MSEA), volcano plots, heatmaps, and pathway analysis.

The analysis compares different clinical groups (e.g., **CvsH: Cancer vs Healthy**, **CvsP: Cancer vs Precancer**) to identify significantly altered metabolites and pathways associated with colorectal cancer.

Use the tabs below to view:
- **Static plots** (Quality PNGs)
- **Interactive visualizations** (Plotly-based figures for deeper exploration)

This tool enables rapid exploration and interpretation of metabolic differences in the context of cancer biology.
""")




static_dir = "results/figures"   # Folder paths
interactive_dir = "streamlit"


png_to_show = [                 
    "PCA_of_Serum_Metabolites.png", 
    "PLS-DA_of_Serum_Metabolites.png", 
    "significant_metabolites_CvsH_&_CvsP.png"
]


def format_plot_title(filename):                               # --- Title formatting helper ---
    name = filename.replace(".json", "").replace("_", " ")

                                                               # Fix group labels and acronyms
    replacements = {                    
        r"\bcvsh\b": "CvsH",
        r"\bcvsp\b": "CvsP",
        r"\bhvsp\b": "HvsP",
        r"\bpls\-da\b": "PLS-DA",
        r"\bpca\b": "PCA"
    }

    for pattern, repl in replacements.items():
        name = re.sub(pattern, repl, name, flags=re.IGNORECASE)

                                                                # Capitalize remaining words (but don't change acronyms or CvsX labels)
    words = name.split()
    final_words = []
    for word in words:
        if word in ["PCA", "PLS-DA", "CvsH", "CvsP", "HvsP", "&"]:
            final_words.append(word)
        else:
            final_words.append(word.capitalize())

    return " ".join(final_words)

# Tabs
tab1, tab2 = st.tabs(["Static Plots", "Interactive Plots"])

                                                              # --- Tab 1: Static Plots ---
with tab1:
    
    for img_file in png_to_show:
        path = os.path.join(static_dir, img_file)
        if os.path.exists(path):
            title = img_file.replace(".png", "").replace("_", " ")
            st.subheader(format_plot_title(title))
            image = Image.open(path)
            st.image(image, use_container_width=True)
        else:
            st.warning(f"File not found: {img_file}")

                                                                    # --- Tab 2: Interactive JSON Plots ---
with tab2:
    
    if not os.path.exists(interactive_dir):
        st.info("Interactive directory not found.")
    else:
        json_files = [f for f in os.listdir(interactive_dir) if f.endswith(".json")]

        if not json_files:
            st.info("No JSON plots found in interactive/")
        else:
            for json_file in sorted(json_files):
                st.subheader(format_plot_title(json_file))
                file_path = os.path.join(interactive_dir, json_file)

                try:
                    with open(file_path, "r") as f:
                        plot_dict = json.load(f)

                                                                          # Remove 'heatmapgl' from layout.template
                    template_data = (
                        plot_dict.get("layout", {})
                        .get("template", {})
                        .get("data", {})
                    )
                    if "heatmapgl" in template_data:
                        template_data.pop("heatmapgl", None)

                    
                    for trace in plot_dict.get("data", []):
                        if trace.get("type") == "heatmapgl":
                            trace["type"] = "heatmap"

                    fig = go.Figure(plot_dict)
                    st.plotly_chart(fig, use_container_width=True, key=json_file)

                except Exception as e:
                    st.error(f"Failed to load {json_file}: {e}")
