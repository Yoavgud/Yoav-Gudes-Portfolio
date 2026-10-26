import base64, re, os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(SCRIPT_DIR, "imgs")
RES_DIR = os.path.join(SCRIPT_DIR, "resumes")
TEMPLATE = os.path.join(SCRIPT_DIR, "portfolio_template.html")
OUTPUT = os.path.join(SCRIPT_DIR, "portfolio.html")

tokens = {
    "__IMG_BOONTON_CAPACITANCE_METER_AND_AGILENT_PARAMETER__": "boonton_capacitance_meter_and_agilent_parameter.jpg",
    "__IMG_CLASSIFICATION_REPORT_TABLES_COMPARING_THREE_MODELS__": "classification_report_tables_comparing_three_models.jpg",
    "__IMG_COPPER_HEAT_PIPE_AND_VAPOR_CHAMBER__": "copper_heat_pipe_and_vapor_chamber.jpg",
    "__IMG_FINISHED_3_INCH_SILICON_WAFER_PATTERNED__": "finished_3_inch_silicon_wafer_patterned.jpg",
    "__IMG_FINISHED_3_INCH_SILICON_WAFER_PATTERNED_2__": "finished_3_inch_silicon_wafer_patterned_2.jpg",
    "__IMG_GE_HEALTHCARE_PRODUCT_CATALOG_PAGE_LISTING__": "ge_healthcare_product_catalog_page_listing.jpg",
    "__IMG_MANUAL_WAFER_PROBE_STATION_WITH_BINOCULAR__": "manual_wafer_probe_station_with_binocular.jpg",
    "__IMG_MICROSCOPE_VIEW_OF_PROBE_NEEDLES_CONTACTING__": "microscope_view_of_probe_needles_contacting.jpg",
    "__IMG_NVIDIA_GM204_MOBILE_GPU_MODULE_REMOVED__": "nvidia_gm204_mobile_gpu_module_removed.jpg",
    "__IMG_NVIDIA_GPU_MODULE_ON_A_TEST__": "nvidia_gpu_module_on_a_test.jpg",
    "__IMG_OSCILLOSCOPE_SCREEN_SHOWING_A_TRIANGLE_WAVE__": "oscilloscope_screen_showing_a_triangle_wave.jpg",
    "__IMG_OSCILLOSCOPE_XY_MODE_SHOWING_A_DIODE__": "oscilloscope_xy_mode_showing_a_diode.jpg",
    "__IMG_SIX_VIALS_OF_CDSE_QUANTUM_DOTS__": "six_vials_of_cdse_quantum_dots.jpg",
    "__IMG_SIX_VIALS_OF_QUANTUM_DOT_SOLUTION__": "six_vials_of_quantum_dot_solution.jpg",
    "__IMG_SIX_VIALS_OF_QUANTUM_DOT_SOLUTION_2__": "six_vials_of_quantum_dot_solution_2.jpg",
    "__IMG_THREE_STUDENTS_IN_CLEANROOM_BUNNY_SUITS__": "three_students_in_cleanroom_bunny_suits.jpg",
    "__IMG_YOAV_STANDING_WITH_TWO_WOLF_ADVANCED__": "yoav_standing_with_two_wolf_advanced.jpg",
    "__IMG_ZOOMED_IN_VIEW_OF_PROBE_TIPS__": "zoomed_in_view_of_probe_tips.jpg",
}

pdf_tokens = {
    "__RESUME_HW_B64__": os.path.join(RES_DIR, "Yoav_Gudes_Semiconductor_Engineering_Resume.pdf"),
    "__RESUME_SW_B64__": os.path.join(RES_DIR, "Yoav_Gudes_AI-ML_Engineering_Resume.pdf"),
    "__RESUME_MIX_B64__": os.path.join(RES_DIR, "Yoav_Gudes_AI-ML_and_Semiconductor_Engineering_Resume.pdf"),
}

with open(TEMPLATE, "r", encoding="utf-8") as f:
    html = f.read()

for token, path in pdf_tokens.items():
    with open(path, "rb") as pf:
        b64 = base64.b64encode(pf.read()).decode("ascii")
    count = html.count(token)
    if count == 0:
        print(f"WARNING: token {token} not found in template")
    html = html.replace(token, b64)

for token, fname in tokens.items():
    path = os.path.join(IMG_DIR, fname)
    with open(path, "rb") as imgf:
        b64 = base64.b64encode(imgf.read()).decode("ascii")
    data_uri = f"data:image/jpeg;base64,{b64}"
    count = html.count(token)
    if count == 0:
        print(f"WARNING: token {token} not found in template")
    html = html.replace(token, data_uri)

leftover = re.findall(r"__[A-Z_]+__", html)
if leftover:
    print("WARNING: leftover tokens:", set(leftover))
else:
    print("All tokens replaced successfully.")

with open(OUTPUT, "w", encoding="utf-8") as f:
    f.write(html)

print("Output size (bytes):", len(html.encode("utf-8")))
