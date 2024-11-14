"""
Rules:
    - User Roles: support, sales, marketing, finance, engineering, hr, product, legal, operations, it
    - Access Levels: database, reporting, user_managment, file, project_managment, finances, sys_config, security

    Use tests below as a guide to write the function (All 80 must pass in order to complete the task)

    Challenge: Try to complete the task without stacking if statements
    Extra challenge (optional): Try not to have more than 10 lines of code inside the function
"""


def display_user_rights(role,access_level):
    rights = {
        'support': {'database': 'read_only', 'reporting': 'view_reports', 'user_managment': 'basic_interaction', 'file': 'view_files', 'project_managment': 'view_projects', 'finances': 'none', 'sys_config': 'view_settings', 'security': 'view_logs'},
        'sales': {'database': 'edit', 'reporting': 'generate_reports', 'user_managment': 'basic_interaction', 'file': 'edit_files', 'project_managment': 'task_managment', 'finances': 'budget_managment', 'sys_config': 'basic_config', 'security': 'none'},
        'marketing': {'database': 'read_only', 'reporting': 'full_control', 'user_managment': 'none', 'file': 'manage_files', 'project_managment': 'project_admin', 'finances': 'view_financials', 'sys_config': 'admin_config', 'security': 'view_logs'},
        'finance': {'database': 'full_control', 'reporting': 'generate_reports', 'user_managment': 'none', 'file': 'view_files', 'project_managment': 'view_projects', 'finances': 'full_control', 'sys_config': 'admin_config', 'security': 'audit_access'},
        'engineering': {'database': 'edit', 'reporting': 'generate_reports', 'user_managment': 'basic_interaction', 'file': 'full_control', 'project_managment': 'full_project_control', 'finances': 'none', 'sys_config': 'full_system_control', 'security': 'policy_managment'},
        'hr': {'database': 'none', 'reporting': 'generate_reports', 'user_managment': 'full_control', 'file': 'edit_files', 'project_managment': 'project_admin', 'finances': 'approval_auth', 'sys_config': 'admin_config', 'security': 'audit_access'},
        'product': {'database': 'edit', 'reporting': 'generate_reports', 'user_managment': 'basic_interaction', 'file': 'manage_files', 'project_managment': 'full_project_control', 'finances': 'view_financials', 'sys_config': 'admin_config', 'security': 'view_logs'},
        'legal': {'database': 'none', 'reporting': 'view_reports', 'user_managment': 'none', 'file': 'view_files', 'project_managment': 'view_projects', 'finances': 'approval_auth', 'sys_config': 'policy_managment', 'security': 'full_control'},
        'operations': {'database': 'full_control', 'reporting': 'generate_reports', 'user_managment': 'basic_interaction', 'file': 'full_control', 'project_managment': 'task_managment', 'finances': 'budget_managment', 'sys_config': 'admin_config', 'security': 'view_logs'},
        'it': {'database': 'full_control', 'reporting': 'full_control', 'user_managment': 'user_managment', 'file': 'full_control', 'project_managment': 'project_admin', 'finances': 'none', 'sys_config': 'full_control', 'security': 'full_control'}
    }
    
    return rights.get(role).get(access_level)




# Don't change the code below this line


pass_count = 0
if display_user_rights('support', 'database') == 'read_only':
    pass_count += 1
if display_user_rights('support', 'reporting') == 'view_reports':
    pass_count += 1
if display_user_rights('support', 'user_managment') == 'basic_interaction':
    pass_count += 1
if display_user_rights('support', 'file') == 'view_files':
    pass_count += 1
if display_user_rights('support', 'project_managment') == 'view_projects':
    pass_count += 1
if display_user_rights('support', 'finances') == 'none':
    pass_count += 1
if display_user_rights('support', 'sys_config') == 'view_settings':
    pass_count += 1
if display_user_rights('support', 'security') == 'view_logs':
    pass_count += 1

if display_user_rights('sales', 'database') == 'edit':
    pass_count += 1
if display_user_rights('sales', 'reporting') == 'generate_reports':
    pass_count += 1
if display_user_rights('sales', 'user_managment') == 'basic_interaction':
    pass_count += 1
if display_user_rights('sales', 'file') == 'edit_files':
    pass_count += 1
if display_user_rights('sales', 'project_managment') == 'task_managment':
    pass_count += 1
if display_user_rights('sales', 'finances') == 'budget_managment':
    pass_count += 1
if display_user_rights('sales', 'sys_config') == 'basic_config':
    pass_count += 1
if display_user_rights('sales', 'security') == 'none':
    pass_count += 1

if display_user_rights('marketing', 'database') == 'read_only':
    pass_count += 1
if display_user_rights('marketing', 'reporting') == 'full_control':
    pass_count += 1
if display_user_rights('marketing', 'user_managment') == 'none':
    pass_count += 1
if display_user_rights('marketing', 'file') == 'manage_files':
    pass_count += 1
if display_user_rights('marketing', 'project_managment') == 'project_admin':
    pass_count += 1
if display_user_rights('marketing', 'finances') == 'view_financials':
    pass_count += 1
if display_user_rights('marketing', 'sys_config') == 'admin_config':
    pass_count += 1
if display_user_rights('marketing', 'security') == 'view_logs':
    pass_count += 1

if display_user_rights('finance', 'database') == 'full_control':
    pass_count += 1
if display_user_rights('finance', 'reporting') == 'generate_reports':
    pass_count += 1
if display_user_rights('finance', 'user_managment') == 'none':
    pass_count += 1
if display_user_rights('finance', 'file') == 'view_files':
    pass_count += 1
if display_user_rights('finance', 'project_managment') == 'view_projects':
    pass_count += 1
if display_user_rights('finance', 'finances') == 'full_control':
    pass_count += 1
if display_user_rights('finance', 'sys_config') == 'admin_config':
    pass_count += 1
if display_user_rights('finance', 'security') == 'audit_access':
    pass_count += 1

if display_user_rights('engineering', 'database') == 'edit':
    pass_count += 1
if display_user_rights('engineering', 'reporting') == 'generate_reports':
    pass_count += 1
if display_user_rights('engineering', 'user_managment') == 'basic_interaction':
    pass_count += 1
if display_user_rights('engineering', 'file') == 'full_control':
    pass_count += 1
if display_user_rights('engineering', 'project_managment') == 'full_project_control':
    pass_count += 1
if display_user_rights('engineering', 'finances') == 'none':
    pass_count += 1
if display_user_rights('engineering', 'sys_config') == 'full_system_control':
    pass_count += 1
if display_user_rights('engineering', 'security') == 'policy_managment':
    pass_count += 1

if display_user_rights('hr', 'database') == 'none':
    pass_count += 1
if display_user_rights('hr', 'reporting') == 'generate_reports':
    pass_count += 1
if display_user_rights('hr', 'user_managment') == 'full_control':
    pass_count += 1
if display_user_rights('hr', 'file') == 'edit_files':
    pass_count += 1
if display_user_rights('hr', 'project_managment') == 'project_admin':
    pass_count += 1
if display_user_rights('hr', 'finances') == 'approval_auth':
    pass_count += 1
if display_user_rights('hr', 'sys_config') == 'admin_config':
    pass_count += 1
if display_user_rights('hr', 'security') == 'audit_access':
    pass_count += 1

if display_user_rights('product', 'database') == 'edit':
    pass_count += 1
if display_user_rights('product', 'reporting') == 'generate_reports':
    pass_count += 1
if display_user_rights('product', 'user_managment') == 'basic_interaction':
    pass_count += 1
if display_user_rights('product', 'file') == 'manage_files':
    pass_count += 1
if display_user_rights('product', 'project_managment') == 'full_project_control':
    pass_count += 1
if display_user_rights('product', 'finances') == 'view_financials':
    pass_count += 1
if display_user_rights('product', 'sys_config') == 'admin_config':
    pass_count += 1
if display_user_rights('product', 'security') == 'view_logs':
    pass_count += 1

if display_user_rights('legal', 'database') == 'none':
    pass_count += 1
if display_user_rights('legal', 'reporting') == 'view_reports':
    pass_count += 1
if display_user_rights('legal', 'user_managment') == 'none':
    pass_count += 1
if display_user_rights('legal', 'file') == 'view_files':
    pass_count += 1
if display_user_rights('legal', 'project_managment') == 'view_projects':
    pass_count += 1
if display_user_rights('legal', 'finances') == 'approval_auth':
    pass_count += 1
if display_user_rights('legal', 'sys_config') == 'policy_managment':
    pass_count += 1
if display_user_rights('legal', 'security') == 'full_control':
    pass_count += 1

if display_user_rights('operations', 'database') == 'full_control':
    pass_count += 1
if display_user_rights('operations', 'reporting') == 'generate_reports':
    pass_count += 1
if display_user_rights('operations', 'user_managment') == 'basic_interaction':
    pass_count += 1
if display_user_rights('operations', 'file') == 'full_control':
    pass_count += 1
if display_user_rights('operations', 'project_managment') == 'task_managment':
    pass_count += 1
if display_user_rights('operations', 'finances') == 'budget_managment':
    pass_count += 1
if display_user_rights('operations', 'sys_config') == 'admin_config':
    pass_count += 1
if display_user_rights('operations', 'security') == 'view_logs':
    pass_count += 1

if display_user_rights('it', 'database') == 'full_control':
    pass_count += 1
if display_user_rights('it', 'reporting') == 'full_control':
    pass_count += 1
if display_user_rights('it', 'user_managment') == 'user_managment':
    pass_count += 1
if display_user_rights('it', 'file') == 'full_control':
    pass_count += 1
if display_user_rights('it', 'project_managment') == 'project_admin':
    pass_count += 1
if display_user_rights('it', 'finances') == 'none':
    pass_count += 1
if display_user_rights('it', 'sys_config') == 'full_control':
    pass_count += 1
if display_user_rights('it', 'security') == 'full_control':
    pass_count += 1

print(f"Tests passed: {pass_count}/80")
if pass_count == 80:
    print('All tests passed, TASK COMPLETE!')