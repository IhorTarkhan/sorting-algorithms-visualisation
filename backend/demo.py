from backend.db.sorting_logs_connector import create_table_if_not_exist, get_all_sorting_logs

if __import__('__main__'):
    create_table_if_not_exist()
    logs = get_all_sorting_logs()
