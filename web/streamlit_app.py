"""
MarkFlow - Modern Markdown to PDF Converter (Web Demo)

Copyright (c) 2025 Raja Namdeo <cse.rajanamdeo@gmail.com>
All rights reserved.

This file is part of MarkFlow, a modern Markdown to PDF converter.
"""

import streamlit as st
from pathlib import Path
import sys

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from md_to_pdf.core import convert_to_pdf

# Page config
st.set_page_config(
    page_title="MarkFlow - Markdown to PDF Converter",
    page_icon="📝",
    layout="wide"
)

# Title and description
st.title("🌟 MarkFlow Online")
st.markdown("""
Convert your Markdown to beautifully formatted PDFs instantly!

Created by [Raja Namdeo](mailto:cse.rajanamdeo@gmail.com)
""")

# Two-column layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 Input Markdown")
    markdown_text = st.text_area(
        "Enter your Markdown here",
        height=400,
        placeholder="# Hello MarkFlow!\n\nStart typing your markdown here..."
    )
    
    # Style options
    st.subheader("🎨 Style Options")
    theme = st.selectbox(
        "Choose theme",
        ["Default", "Modern", "Academic", "Business"]
    )
    
    font = st.selectbox(
        "Font family",
        ["Arial", "Times New Roman", "Roboto", "Open Sans"]
    )

with col2:
    st.subheader("👁️ Preview")
    if markdown_text:
        try:
            # Convert to PDF
            pdf_bytes = convert_to_pdf(
                markdown_text,
                theme=theme.lower(),
                font=font
            )
            
            # Show success message
            st.success("✨ Conversion successful!")
            
            # Download button
            st.download_button(
                "⬇️ Download PDF",
                pdf_bytes,
                file_name="markflow_output.pdf",
                mime="application/pdf"
            )
            
            # Preview (if possible)
            st.markdown("### PDF Preview")
            st.markdown(markdown_text)
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
    else:
        st.info("Enter some markdown text to see the preview!")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>Made with ❤️ by Raja Namdeo</p>
    <p>
        <a href='https://github.com/yourusername/markflow'>GitHub</a> •
        <a href='https://markflow.readthedocs.io'>Documentation</a> •
        <a href='mailto:cse.rajanamdeo@gmail.com'>Contact</a>
    </p>
</div>
""", unsafe_allow_html=True)
