BASE_PATH = "/Volumes/workspace/bronze/source_system"

INGESTION_CONFIG = [
    # CRM
    {
        "source": "crm",
        "path": f"{BASE_PATH}/Source CRM/cust_info.csv",
        "table": "crm_cust_info_raw"
    },
    {
        "source": "crm",
        "path": f"{BASE_PATH}/Source CRM/prd_info.csv",
        "table": "crm_prd_info_raw"
    },
    {
        "source": "crm",
        "path": f"{BASE_PATH}/Source CRM/sales_details.csv",
        "table": "crm_sales_details_raw"
    },

    # ERP
    {
        "source": "erp",
        "path": f"{BASE_PATH}/Source ERP/CUST_AZ12.csv",
        "table": "erp_cust_az12_raw"
    },
    {
        "source": "erp",
        "path": f"{BASE_PATH}/Source ERP/LOC_A101.csv",
        "table": "erp_loc_a101_raw"
    },
    {
        "source": "erp",
        "path": f"{BASE_PATH}/Source ERP/PX_CAT_G1V2.csv",
        "table": "erp_px_cat_g1v2_raw"
    }
]
