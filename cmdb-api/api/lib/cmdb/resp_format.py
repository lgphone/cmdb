# -*- coding:utf-8 -*-

from api.lib.resp_format import CommonErrFormat


class ErrFormat(CommonErrFormat):
    ci_type_config = "模型配置"

    invalid_relation_type = "无效的关系类型: {}"
    ci_type_not_found = "模型不存在!"
    argument_attributes_must_be_list = "参数 attributes 类型必须是列表"
    argument_file_not_found = "文件似乎并未上传"

    attribute_not_found = "属性 {} 不存在!"
    attribute_is_unique_id = "该属性是模型的唯一标识，不能被删除!"
    attribute_is_ref_by_type = "该属性被模型 {} 引用, 不能删除!"
    attribute_value_type_cannot_change = "属性的值类型不允许修改!"
    attribute_list_value_cannot_change = "多值不被允许修改!"
    attribute_index_cannot_change = "修改索引 非管理员不被允许!"
    attribute_index_change_failed = "索引切换失败!"
    invalid_choice_values = "预定义值的类型不对！"
    attribute_name_duplicate = "重复的属性名 {}"
    add_attribute_failed = "创建属性 {} 失败!"
    update_attribute_failed = "修改属性 {} 失败!"
    cannot_edit_attribute = "您没有权限修改该属性!"
    cannot_delete_attribute = "目前只允许 属性创建人、管理员 删除属性!"
    attribute_name_cannot_be_builtin = "属性字段名不能是内置字段: id, _id, ci_id, type, _type, ci_type"
    attribute_choice_other_invalid = "预定义值: 其他模型请求参数不合法!"

    ci_not_found = "CI {} 不存在"
    unique_constraint = "多属性联合唯一校验不通过: {}"
    unique_value_not_found = "模型的主键 {} 不存在!"
    unique_key_required = "主键字段 {} 缺失"
    ci_is_already_existed = "CI 已经存在!"
    relation_constraint = "关系约束: {}, 校验失败 "
    m2m_relation_constraint = "多对多关系 限制: 模型 {} <-> {} 已经存在多对多关系!"
    relation_not_found = "CI关系: {} 不存在"
    ci_search_Parentheses_invalid = "搜索表达式里小括号前不支持: 或、非"

    ci_type_not_found2 = "模型 {} 不存在"
    ci_type_is_already_existed = "模型 {} 已经存在"
    unique_key_not_define = "主键未定义或者已被删除"
    only_owner_can_delete = "只有创建人才能删除它!"
    ci_exists_and_cannot_delete_type = "因为CI已经存在，不能删除模型"
    ci_relation_view_exists_and_cannot_delete_type = "因为关系视图 {} 引用了该模型，不能删除模型"
    ci_type_group_not_found = "模型分组 {} 不存在"
    ci_type_group_exists = "模型分组 {} 已经存在"
    ci_type_relation_not_found = "模型关系 {} 不存在"
    ci_type_attribute_group_duplicate = "属性分组 {} 已存在"
    ci_type_attribute_group_not_found = "属性分组 {} 不存在"
    ci_type_group_attribute_not_found = "属性组<{0}> - 属性<{1}> 不存在"
    unique_constraint_duplicate = "唯一约束已经存在!"
    unique_constraint_invalid = "唯一约束的属性不能是 JSON 和 多值"
    ci_type_trigger_duplicate = "重复的触发器"
    ci_type_trigger_not_found = "触发器 {} 不存在"

    record_not_found = "操作记录 {} 不存在"
    cannot_delete_unique = "不能删除唯一标识"
    cannot_delete_default_order_attr = "不能删除默认排序的属性"

    preference_relation_view_node_required = "没有选择节点"
    preference_search_option_not_found = "该搜索选项不存在!"
    preference_search_option_exists = "该搜索选项命名重复!"

    relation_type_exists = "关系类型 {} 已经存在"
    relation_type_not_found = "关系类型 {} 不存在"

    attribute_value_invalid = "无效的属性值: {}"
    attribute_value_invalid2 = "{} 无效的值: {}"
    not_in_choice_values = "{} 不在预定义值里"
    attribute_value_unique_required = "属性 {} 的值必须是唯一的, 当前值 {} 已存在"
    attribute_value_required = "属性 {} 值必须存在"
    attribute_value_unknown_error = "新增或者修改属性值未知错误: {}"

    custom_name_duplicate = "订制名重复"

    limit_ci_type = "模型数超过限制: {}"
    limit_ci = "CI数超过限制: {}"

    adr_duplicate = "自动发现规则: {} 已经存在!"
    adr_not_found = "自动发现规则: {} 不存在!"
    adr_referenced = "该自动发现规则被模型引用, 不能删除!"
    ad_duplicate = "自动发现规则的应用不能重复定义!"
    ad_not_found = "您要修改的自动发现: {} 不存在!"
    ad_not_unique_key = "属性字段没有包括唯一标识: {}"
    adc_not_found = "自动发现的实例不存在!"
    adt_not_found = "模型并未关联该自动发现!"
    adt_secret_no_permission = "只有创建人才能修改Secret!"
    cannot_delete_adt = "该规则已经有自动发现的实例, 不能被删除!"
    adr_default_ref_once = "该默认的自动发现规则 已经被模型 {} 引用!"
    adr_unique_key_required = "unique_key方法必须返回非空字符串!"
    adr_plugin_attributes_list_required = "attributes方法必须返回的是list"
    adr_plugin_attributes_list_no_empty = "attributes方法返回的list不能为空!"
    adt_target_all_no_permission = "只有管理员才可以定义执行机器为: 所有节点!"
    adt_target_expr_no_permission = "执行机器权限检查不通过: {}"

    ci_filter_name_cannot_be_empty = "CI过滤授权 必须命名!"
    ci_filter_perm_cannot_or_query = "CI过滤授权 暂时不支持 或 查询"
    ci_filter_perm_attr_no_permission = "您没有属性 {} 的操作权限!"
    ci_filter_perm_ci_no_permission = "您没有该CI的操作权限!"

    password_save_failed = "保存密码失败: {}"
    password_load_failed = "获取密码失败: {}"
