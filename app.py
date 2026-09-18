import streamlit as st
import pandas as pd
from datetime import datetime, date
import plotly.express as px
import os

# --- Page Configuration ---
st.set_page_config(
    page_title="MedCabinet - Home Medicine Analytics",
    page_icon="💊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSV Data Persistence Configuration ---
DATA_FILE = "medicines.csv"

DEFAULT_DATA = [
    {
        "id": "med-1",
        "name_zh": "布洛芬缓释胶囊",
        "name_en": "Ibuprofen Extended-Release Capsules",
        "category_key": "antipyretic",
        "dosage_form_zh": "缓释胶囊",
        "dosage_form_en": "Capsule",
        "indications_zh": "发烧, 偏头痛, 牙痛, 关节痛, 痛经",
        "indications_en": "Fever, Migraine, Toothache, Joint pain, Dysmenorrhea",
        "expiry_date": "2027-03-15",
        "storage_zh": "常温药箱",
        "storage_en": "Room Temp Cabinet",
        "notes": "Fenbid, 2x daily after food"
    },
    {
        "id": "med-2",
        "name_zh": "阿莫西林胶囊",
        "name_en": "Amoxicillin Capsules",
        "category_key": "antibiotic",
        "dosage_form_zh": "胶囊",
        "dosage_form_en": "Capsule",
        "indications_zh": "扁桃体炎, 中耳炎, 呼吸道感染",
        "indications_en": "Tonsillitis, Otitis media, Respiratory infection",
        "expiry_date": "2026-10-15",
        "storage_zh": "常温药箱",
        "storage_en": "Room Temp Cabinet",
        "notes": "Check penicillin allergy"
    },
    {
        "id": "med-3",
        "name_zh": "蒙脱石散",
        "name_en": "Montmorillonite Powder",
        "category_key": "gastro",
        "dosage_form_zh": "散剂",
        "dosage_form_en": "Powder",
        "indications_zh": "急性腹泻, 拉肚子, 胃肠保护",
        "indications_en": "Acute diarrhea, GI protection",
        "expiry_date": "2027-09-01",
        "storage_zh": "常温药箱",
        "storage_en": "Room Temp Cabinet",
        "notes": "Take between meals"
    },
    {
        "id": "med-4",
        "name_zh": "氯雷他定片",
        "name_en": "Loratadine Tablets",
        "category_key": "respiratory",
        "dosage_form_zh": "片剂",
        "dosage_form_en": "Tablet",
        "indications_zh": "过敏性鼻炎, 荨麻疹, 喷嚏, 皮肤瘙痒",
        "indications_en": "Allergic rhinitis, Urticaria, Sneezing, Skin itch",
        "expiry_date": "2026-10-30",
        "storage_zh": "床头应急盒",
        "storage_en": "Bedroom Box",
        "notes": "Non-drowsy antihistamine"
    },
    {
        "id": "med-5",
        "name_zh": "重组人干扰素α2b凝胶",
        "name_en": "Interferon Alfa-2b Gel",
        "category_key": "antibiotic",
        "dosage_form_zh": "凝胶",
        "dosage_form_en": "Topical Gel",
        "indications_zh": "单纯疱疹, 口唇疱疹",
        "indications_en": "Herpes simplex, Cold sores",
        "expiry_date": "2026-05-10",
        "storage_zh": "冰箱冷藏 (2-8℃)",
        "storage_en": "Refrigerator (2-8°C)",
        "notes": "Keep refrigerated"
    },
    {
        "id": "med-6",
        "name_zh": "医用碘伏棉棒",
        "name_en": "Povidone Iodine Cotton Swabs",
        "category_key": "firstaid",
        "dosage_form_zh": "外用棉棒",
        "dosage_form_en": "Swabs",
        "indications_zh": "擦伤, 割伤, 创口消毒",
        "indications_en": "Cuts, Scratches, Antiseptic disinfection",
        "expiry_date": "2027-12-31",
        "storage_zh": "旅行急救包",
        "storage_en": "Travel First-Aid Kit",
        "notes": "Snap red ring end to use"
    }
]

def load_data():
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE)
    df = pd.DataFrame(DEFAULT_DATA)
    df.to_csv(DATA_FILE, index=False)
    return df

def save_data(df):
    df.to_csv(DATA_FILE, index=False)

# --- Bilingual i18n Dictionary ---
CATEGORIES = {
    "antipyretic": {"zh": "解热镇痛", "en": "Pain & Fever"},
    "antibiotic": {"zh": "抗菌抗炎", "en": "Antibiotics"},
    "gastro": {"zh": "消化肠胃", "en": "Gastrointestinal"},
    "respiratory": {"zh": "呼吸抗敏", "en": "Respiratory & Allergy"},
    "firstaid": {"zh": "外用急救", "en": "First Aid & Wound"},
    "other": {"zh": "其他常用", "en": "Other General"}
}

I18N = {
    "zh": {
        "title": "💊 MedCabinet - 家庭药箱与效期数据看板",
        "subtitle": "家庭常备药品效期监控、症状匹配与数据分析平台",
        "lang_switch": "切换语言 / Language",
        "kpi_total": "备药总品种",
        "kpi_healthy": "正常储存 (>60天)",
        "kpi_expiring": "临期预警 (≤60天)",
        "kpi_expired": "已过期药品",
        "tab_inventory": "📋 药箱检索与数据管理",
        "tab_analytics": "📊 效期分布与统计图表",
        "tab_add": "➕ 登记新药品",
        "search_label": "搜索药品名称或症状标签 (如: 头痛、发热、拉肚子、allergy、fever)",
        "filter_status": "效期状态筛选",
        "filter_category": "功效分类筛选",
        "all": "全部",
        "status_healthy": "正常 (60天+)",
        "status_expiring": "临期 (≤60天)",
        "status_expired": "已过期",
        "col_name": "药品名称",
        "col_cat": "分类",
        "col_form": "剂型",
        "col_indications": "适应症 / 功效",
        "col_storage": "存放位置",
        "col_expiry": "有效期",
        "col_days": "剩余天数",
        "col_status": "当前状态",
        "col_notes": "用法/注意事项",
        "btn_delete": "删除选中药品",
        "form_name_zh": "药品中文名称 *",
        "form_name_en": "药品英文名称",
        "form_cat": "药品分类 *",
        "form_form_zh": "剂型中文 (如: 胶囊、片剂)",
        "form_form_en": "剂型英文 (如: Capsule, Tablet)",
        "form_exp": "有效截止期 *",
        "form_store_zh": "存放位置 (中文)",
        "form_store_en": "存放位置 (英文)",
        "form_ind_zh": "适应症/症状标签 (中文逗号分隔)",
        "form_ind_en": "适应症/症状标签 (英文逗号分隔)",
        "form_notes": "备注 / 用法说明",
        "btn_save": "确认存入药箱",
        "msg_saved": "✅ 药品登记成功！",
        "msg_deleted": "🗑️ 选中的药品记录已删除！",
        "chart_days_hist": "保质期剩余天数直方图 (DS Expiry Bins)",
        "chart_cat_pie": "药品功效分类占比 (Category Ratio)",
        "days_label": "剩余保质期 (天)",
        "count_label": "药品数量",
        "reset_btn": "恢复初始预设数据"
    },
    "en": {
        "title": "💊 MedCabinet - Smart Medicine Inventory & Shelf-Life Analytics",
        "subtitle": "Bilingual Household Medicine Inventory, Expiry Tracking & Exploratory Data Platform",
        "lang_switch": "Language / 切换语言",
        "kpi_total": "Total Medicines",
        "kpi_healthy": "Healthy (>60 Days)",
        "kpi_expiring": "Expiring Soon (≤60 Days)",
        "kpi_expired": "Expired",
        "tab_inventory": "📋 Inventory & Search",
        "tab_analytics": "📊 Analytics & Charts",
        "tab_add": "➕ Register Medication",
        "search_label": "Search medicine name or symptoms (e.g., headache, fever, pain, 止痛)",
        "filter_status": "Expiry Status Filter",
        "filter_category": "Category Filter",
        "all": "All",
        "status_healthy": "Healthy (>60d)",
        "status_expiring": "Expiring Soon (≤60d)",
        "status_expired": "Expired",
        "col_name": "Medication Name",
        "col_cat": "Category",
        "col_form": "Form",
        "col_indications": "Indications / Symptoms",
        "col_storage": "Storage",
        "col_expiry": "Expiry Date",
        "col_days": "Days Left",
        "col_status": "Status",
        "col_notes": "Directions / Notes",
        "btn_delete": "Delete Selected Medication",
        "form_name_zh": "Chinese Medicine Name *",
        "form_name_en": "English Medicine Name",
        "form_cat": "Category *",
        "form_form_zh": "Dosage Form (Chinese)",
        "form_form_en": "Dosage Form (English)",
        "form_exp": "Expiration Date *",
        "form_store_zh": "Storage Location (Chinese)",
        "form_store_en": "Storage Location (English)",
        "form_ind_zh": "Indications (Chinese, comma-separated)",
        "form_ind_en": "Indications (English, comma-separated)",
        "form_notes": "Directions / Doctor Notes",
        "btn_save": "Save Medication",
        "msg_saved": "✅ Medication added successfully!",
        "msg_deleted": "🗑️ Selected item deleted!",
        "chart_days_hist": "Shelf-Life Days Left Histogram (DS Expiry Bins)",
        "chart_cat_pie": "Category Distribution Ratio",
        "days_label": "Days Remaining",
        "count_label": "Count",
        "reset_btn": "Reset to Sample Data"
    }
}

# --- Sidebar Controls ---
with st.sidebar:
    st.header("⚙️ Settings")
    lang_choice = st.radio("🌐 Language / 语言", ["中文", "English"], horizontal=True)
    lang = "zh" if lang_choice == "中文" else "en"
    t = I18N[lang]

    st.markdown("---")
    if st.button(t["reset_btn"]):
        if os.path.exists(DATA_FILE):
            os.remove(DATA_FILE)
        st.session_state.df = load_data()
        st.rerun()

# --- Initialize State ---
if "df" not in st.session_state:
    st.session_state.df = load_data()

df = st.session_state.df.copy()

# Feature Engineering: compute days left & status
today = date.today()
df["expiry_dt"] = pd.to_datetime(df["expiry_date"]).dt.date
df["days_left"] = (df["expiry_dt"] - today).apply(lambda x: x.days)

def classify_status(days):
    if days < 0:
        return "expired"
    elif days <= 60:
        return "expiring"
    return "healthy"

df["status_code"] = df["days_left"].apply(classify_status)

status_label_map = {
    "healthy": t["status_healthy"],
    "expiring": t["status_expiring"],
    "expired": t["status_expired"]
}
df["display_status"] = df["status_code"].map(status_label_map)

# Localized Display Columns
df["display_name"] = df.apply(
    lambda r: f"{r['name_zh']} ({r['name_en']})" if pd.notna(r['name_en']) and str(r['name_en']).strip() else r['name_zh'],
    axis=1
) if lang == "zh" else df.apply(
    lambda r: f"{r['name_en']} ({r['name_zh']})" if pd.notna(r['name_zh']) and str(r['name_zh']).strip() else r['name_en'],
    axis=1
)

df["display_cat"] = df["category_key"].apply(lambda k: CATEGORIES.get(k, {}).get(lang, k))
df["display_form"] = df[f"dosage_form_{lang}"]
df["display_storage"] = df[f"storage_{lang}"]
df["display_indications"] = df[f"indications_{lang}"]

# --- App Header ---
st.title(t["title"])
st.caption(t["subtitle"])

# --- KPI Metric Cards ---
col1, col2, col3, col4 = st.columns(4)
total_count = len(df)
healthy_count = len(df[df["status_code"] == "healthy"])
expiring_count = len(df[df["status_code"] == "expiring"])
expired_count = len(df[df["status_code"] == "expired"])

col1.metric(t["kpi_total"], total_count)
col2.metric(t["kpi_healthy"], healthy_count, delta=f"{(healthy_count/total_count*100):.0f}%" if total_count > 0 else "0%")
col3.metric(t["kpi_expiring"], expiring_count, delta=f"-{expiring_count}" if expiring_count > 0 else "0", delta_color="inverse")
col4.metric(t["kpi_expired"], expired_count, delta=f"-{expired_count}" if expired_count > 0 else "0", delta_color="inverse")

st.markdown("---")

# --- Tabs ---
tab_list, tab_charts, tab_new = st.tabs([t["tab_inventory"], t["tab_analytics"], t["tab_add"]])

# === Tab 1: Inventory List & Search ===
with tab_list:
    c_search, c_filter1, c_filter2 = st.columns([2, 1, 1])
    with c_search:
        query = st.text_input(f"🔍 {t['search_label']}", "")
    with c_filter1:
        status_opts = [t["all"], t["status_healthy"], t["status_expiring"], t["status_expired"]]
        selected_status = st.selectbox(t["filter_status"], status_opts)
    with c_filter2:
        cat_choices = [t["all"]] + [v[lang] for v in CATEGORIES.values()]
        selected_cat = st.selectbox(t["filter_category"], cat_choices)

    filtered = df.copy()

    # Search filter across bilingual fields
    if query:
        q = query.strip().lower()
        filtered = filtered[
            filtered["name_zh"].astype(str).str.lower().str.contains(q) |
            filtered["name_en"].astype(str).str.lower().str.contains(q) |
            filtered["indications_zh"].astype(str).str.lower().str.contains(q) |
            filtered["indications_en"].astype(str).str.lower().str.contains(q) |
            filtered["notes"].astype(str).str.lower().str.contains(q)
        ]

    # Status filter
    if selected_status != t["all"]:
        filtered = filtered[filtered["display_status"] == selected_status]

    # Category filter
    if selected_cat != t["all"]:
        filtered = filtered[filtered["display_cat"] == selected_cat]

    # Render Table
    show_cols = [
        "display_name", "display_cat", "display_form", "display_indications",
        "display_storage", "expiry_date", "days_left", "display_status", "notes"
    ]
    col_names_map = {
        "display_name": t["col_name"],
        "display_cat": t["col_cat"],
        "display_form": t["col_form"],
        "display_indications": t["col_indications"],
        "display_storage": t["col_storage"],
        "expiry_date": t["col_expiry"],
        "days_left": t["col_days"],
        "display_status": t["col_status"],
        "notes": t["col_notes"]
    }

    display_df = filtered[show_cols].rename(columns=col_names_map).sort_values(by=t["col_days"])
    st.dataframe(display_df, use_container_width=True, hide_index=True)

    # Delete Section
    with st.expander(t["btn_delete"]):
        med_to_delete = st.selectbox(
            t["col_name"],
            options=df["id"].tolist(),
            format_func=lambda x: df[df["id"] == x]["display_name"].values[0] if len(df[df["id"] == x]) > 0 else x
        )
        if st.button("🗑️ " + t["btn_delete"]):
            st.session_state.df = df[df["id"] != med_to_delete].drop(columns=["expiry_dt", "days_left", "status_code", "display_status", "display_name", "display_cat", "display_form", "display_storage", "display_indications"])
            save_data(st.session_state.df)
            st.success(t["msg_deleted"])
            st.rerun()

# === Tab 2: Analytics & Charts ===
with tab_charts:
    chart_c1, chart_c2 = st.columns(2)

    with chart_c1:
        fig_cat = px.pie(
            df,
            names="display_cat",
            title=t["chart_cat_pie"],
            hole=0.45,
            color_discrete_sequence=px.colors.qualitative.Safe
        )
        fig_cat.update_layout(margin=dict(t=40, b=20, l=20, r=20))
        st.plotly_chart(fig_cat, use_container_width=True)

    with chart_c2:
        # Define expiry bins
        fig_hist = px.histogram(
            df,
            x="days_left",
            nbins=12,
            title=t["chart_days_hist"],
            labels={"days_left": t["days_label"], "count": t["count_label"]},
            color="status_code",
            color_discrete_map={
                "healthy": "#10b981",
                "expiring": "#f59e0b",
                "expired": "#ef4444"
            }
        )
        fig_hist.update_layout(
            bargap=0.1,
            showlegend=False,
            margin=dict(t=40, b=20, l=20, r=20)
        )
        st.plotly_chart(fig_hist, use_container_width=True)

# === Tab 3: Add Medication Form ===
with tab_new:
    with st.form("add_medication_form"):
        fc1, fc2 = st.columns(2)
        with fc1:
            in_name_zh = st.text_input(t["form_name_zh"], placeholder="例如: 布洛芬缓释胶囊")
            in_form_zh = st.text_input(t["form_form_zh"], value="胶囊")
            in_store_zh = st.text_input(t["form_store_zh"], value="常温主药箱")
            in_ind_zh = st.text_input(t["form_ind_zh"], placeholder="例如: 发烧, 偏头痛, 关节痛")
        with fc2:
            in_name_en = st.text_input(t["form_name_en"], placeholder="e.g. Ibuprofen Capsules")
            in_form_en = st.text_input(t["form_form_en"], value="Capsule")
            in_store_en = st.text_input(t["form_store_en"], value="Room Temp Cabinet")
            in_ind_en = st.text_input(t["form_ind_en"], placeholder="e.g. Fever, Migraine, Joint pain")

        gc1, gc2 = st.columns(2)
        with gc1:
            cat_keys = list(CATEGORIES.keys())
            in_cat = st.selectbox(
                t["form_cat"],
                options=cat_keys,
                format_func=lambda x: f"{CATEGORIES[x][lang]} ({CATEGORIES[x]['en']})"
            )
        with gc2:
            in_expiry = st.date_input(t["form_exp"])

        in_notes = st.text_input(t["form_notes"], placeholder="例如: 每日2次, 饭后服 / 2x daily after food")
        submit_btn = st.form_submit_button(t["btn_save"])

        if submit_btn:
            if not in_name_zh.strip() and not in_name_en.strip():
                st.error("Please provide at least a Chinese or English name.")
            else:
                new_row = {
                    "id": f"med-{int(datetime.now().timestamp())}",
                    "name_zh": in_name_zh.strip() if in_name_zh.strip() else in_name_en.strip(),
                    "name_en": in_name_en.strip() if in_name_en.strip() else in_name_zh.strip(),
                    "category_key": in_cat,
                    "dosage_form_zh": in_form_zh.strip(),
                    "dosage_form_en": in_form_en.strip(),
                    "indications_zh": in_ind_zh.strip(),
                    "indications_en": in_ind_en.strip(),
                    "expiry_date": str(in_expiry),
                    "storage_zh": in_store_zh.strip(),
                    "storage_en": in_store_en.strip(),
                    "notes": in_notes.strip()
                }
                base_cols = [
                    "id", "name_zh", "name_en", "category_key", "dosage_form_zh",
                    "dosage_form_en", "indications_zh", "indications_en", "expiry_date",
                    "storage_zh", "storage_en", "notes"
                ]
                clean_base_df = st.session_state.df[base_cols]
                updated_df = pd.concat([clean_base_df, pd.DataFrame([new_row])], ignore_index=True)
                save_data(updated_df)
                st.session_state.df = updated_df
                st.success(t["msg_saved"])
                st.rerun()