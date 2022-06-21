<template>
    <div class="app-container">
        <el-form :model="queryForm" ref="queryForm" size="small" :inline="true" v-show="showSearch"
                 label-width="68px">
            
            <el-form-item label="部门ID" prop="deptId">
                <el-input v-model="queryForm.id" placeholder="请输入主键id" clearable
                          @keyup.enter.native="query"/>
            </el-form-item>
            
            <el-form-item label="部门ID" prop="deptId">
                <el-input v-model="queryForm.create_by" placeholder="请输入创建者id" clearable
                          @keyup.enter.native="query"/>
            </el-form-item>
            
            <el-form-item label="部门ID" prop="deptId">
                <el-input v-model="queryForm.create_time" placeholder="请输入创建时间" clearable
                          @keyup.enter.native="query"/>
            </el-form-item>
            
            <el-form-item label="部门ID" prop="deptId">
                <el-input v-model="queryForm.update_by" placeholder="请输入修改者id" clearable
                          @keyup.enter.native="query"/>
            </el-form-item>
            
            <el-form-item label="部门ID" prop="deptId">
                <el-input v-model="queryForm.update_time" placeholder="请输入修改时间" clearable
                          @keyup.enter.native="query"/>
            </el-form-item>
            
            <el-form-item label="部门ID" prop="deptId">
                <el-input v-model="queryForm.email" placeholder="请输入邮箱" clearable
                          @keyup.enter.native="query"/>
            </el-form-item>
            
            <el-form-item label="部门ID" prop="deptId">
                <el-input v-model="queryForm.entry_date" placeholder="请输入入职日期" clearable
                          @keyup.enter.native="query"/>
            </el-form-item>
            
            <el-form-item label="部门ID" prop="deptId">
                <el-input v-model="queryForm.id_card" placeholder="请输入身份证号" clearable
                          @keyup.enter.native="query"/>
            </el-form-item>
            
            <el-form-item label="部门ID" prop="deptId">
                <el-input v-model="queryForm.id_card_type" placeholder="请输入证件类型" clearable
                          @keyup.enter.native="query"/>
            </el-form-item>
            
            <el-form-item label="部门ID" prop="deptId">
                <el-input v-model="queryForm.no" placeholder="请输入工号" clearable
                          @keyup.enter.native="query"/>
            </el-form-item>
            
            <el-form-item label="部门ID" prop="deptId">
                <el-input v-model="queryForm.org_id" placeholder="请输入部门" clearable
                          @keyup.enter.native="query"/>
            </el-form-item>
            
            <el-form-item label="部门ID" prop="deptId">
                <el-input v-model="queryForm.password" placeholder="请输入密码" clearable
                          @keyup.enter.native="query"/>
            </el-form-item>
            
            <el-form-item label="部门ID" prop="deptId">
                <el-input v-model="queryForm.phone" placeholder="请输入手机号码" clearable
                          @keyup.enter.native="query"/>
            </el-form-item>
            
            <el-form-item label="部门ID" prop="deptId">
                <el-input v-model="queryForm.post_id" placeholder="请输入职位" clearable
                          @keyup.enter.native="query"/>
            </el-form-item>
            
            <el-form-item label="部门ID" prop="deptId">
                <el-input v-model="queryForm.state" placeholder="请输入状态" clearable
                          @keyup.enter.native="query"/>
            </el-form-item>
            
            <el-form-item label="部门ID" prop="deptId">
                <el-input v-model="queryForm.type" placeholder="请输入类型" clearable
                          @keyup.enter.native="query"/>
            </el-form-item>
            
            <el-form-item label="部门ID" prop="deptId">
                <el-input v-model="queryForm.user_name" placeholder="请输入用户名" clearable
                          @keyup.enter.native="query"/>
            </el-form-item>
            
            <el-form-item label="部门ID" prop="deptId">
                <el-input v-model="queryForm.work_hour_system" placeholder="请输入工时制度" clearable
                          @keyup.enter.native="query"/>
            </el-form-item>
            
            <el-form-item>
                <el-button type="primary" icon="el-icon-search" size="mini" @click="query">搜索</el-button>
                <el-button icon="el-icon-refresh" size="mini" @click="queryReset">重置</el-button>
            </el-form-item>
        </el-form>
        <div>
            <el-button type="primary" plain icon="el-icon-plus" size="mini" @click="handleAdd">新增</el-button>
            <el-button type="danger" plain icon="el-icon-delete" size="mini" :disabled="multiple" @click="handleDelete">
                删除
            </el-button>
        </div>
        <el-table v-loading="loading" :data="tableData" @selection-change="handleSelectionChange">
            
            <el-table-column label="主键id" prop="id" width="55" align="center"></el-table-column>
            
            <el-table-column label="创建者id" prop="create_by" width="55" align="center"></el-table-column>
            
            <el-table-column label="创建时间" prop="create_time" width="55" align="center"></el-table-column>
            
            <el-table-column label="修改者id" prop="update_by" width="55" align="center"></el-table-column>
            
            <el-table-column label="修改时间" prop="update_time" width="55" align="center"></el-table-column>
            
            <el-table-column label="邮箱" prop="email" width="55" align="center"></el-table-column>
            
            <el-table-column label="入职日期" prop="entry_date" width="55" align="center"></el-table-column>
            
            <el-table-column label="身份证号" prop="id_card" width="55" align="center"></el-table-column>
            
            <el-table-column label="证件类型" prop="id_card_type" width="55" align="center"></el-table-column>
            
            <el-table-column label="工号" prop="no" width="55" align="center"></el-table-column>
            
            <el-table-column label="部门" prop="org_id" width="55" align="center"></el-table-column>
            
            <el-table-column label="密码" prop="password" width="55" align="center"></el-table-column>
            
            <el-table-column label="手机号码" prop="phone" width="55" align="center"></el-table-column>
            
            <el-table-column label="职位" prop="post_id" width="55" align="center"></el-table-column>
            
            <el-table-column label="状态" prop="state" width="55" align="center"></el-table-column>
            
            <el-table-column label="类型" prop="type" width="55" align="center"></el-table-column>
            
            <el-table-column label="用户名" prop="user_name" width="55" align="center"></el-table-column>
            
            <el-table-column label="工时制度" prop="work_hour_system" width="55" align="center"></el-table-column>
            
            <el-table-column label="操作" align="center" class-name="small-padding fixed-width">
                <template slot-scope="scope">
                    <el-button size="mini" type="text" icon="el-icon-edit" @click="handleUpdate(scope.row)">
                        修改
                    </el-button>
                    <el-button size="mini" type="text" icon="el-icon-delete" @click="handleDelete(scope.row)">
                        删除
                    </el-button>
                </template>
            </el-table-column>
        </el-table>
        <el-pagination @size-change="handleSizeChange" @current-change="handleCurrentChange" :current-page="currentPage"
                       :page-sizes="[10, 20, 50]" :page-size="pagesize" layout="total, sizes, prev, pager, next, jumper"
                       :total="total" style="margin:1rem 0">
        </el-pagination>

        <el-dialog :title="title" :visible.sync="open" width="500px" append-to-body>
            <el-form ref="form" :model="form" :rules="rules" label-width="80px">
                
                <el-form-item label="主键id" prop="deptId">
                    <el-input v-model="form.id" placeholder="请输入主键id"/>
                </el-form-item>
                
                <el-form-item label="创建者id" prop="deptId">
                    <el-input v-model="form.create_by" placeholder="请输入创建者id"/>
                </el-form-item>
                
                <el-form-item label="创建时间" prop="deptId">
                    <el-input v-model="form.create_time" placeholder="请输入创建时间"/>
                </el-form-item>
                
                <el-form-item label="修改者id" prop="deptId">
                    <el-input v-model="form.update_by" placeholder="请输入修改者id"/>
                </el-form-item>
                
                <el-form-item label="修改时间" prop="deptId">
                    <el-input v-model="form.update_time" placeholder="请输入修改时间"/>
                </el-form-item>
                
                <el-form-item label="邮箱" prop="deptId">
                    <el-input v-model="form.email" placeholder="请输入邮箱"/>
                </el-form-item>
                
                <el-form-item label="入职日期" prop="deptId">
                    <el-input v-model="form.entry_date" placeholder="请输入入职日期"/>
                </el-form-item>
                
                <el-form-item label="身份证号" prop="deptId">
                    <el-input v-model="form.id_card" placeholder="请输入身份证号"/>
                </el-form-item>
                
                <el-form-item label="证件类型" prop="deptId">
                    <el-input v-model="form.id_card_type" placeholder="请输入证件类型"/>
                </el-form-item>
                
                <el-form-item label="工号" prop="deptId">
                    <el-input v-model="form.no" placeholder="请输入工号"/>
                </el-form-item>
                
                <el-form-item label="部门" prop="deptId">
                    <el-input v-model="form.org_id" placeholder="请输入部门"/>
                </el-form-item>
                
                <el-form-item label="密码" prop="deptId">
                    <el-input v-model="form.password" placeholder="请输入密码"/>
                </el-form-item>
                
                <el-form-item label="手机号码" prop="deptId">
                    <el-input v-model="form.phone" placeholder="请输入手机号码"/>
                </el-form-item>
                
                <el-form-item label="职位" prop="deptId">
                    <el-input v-model="form.post_id" placeholder="请输入职位"/>
                </el-form-item>
                
                <el-form-item label="状态" prop="deptId">
                    <el-input v-model="form.state" placeholder="请输入状态"/>
                </el-form-item>
                
                <el-form-item label="类型" prop="deptId">
                    <el-input v-model="form.type" placeholder="请输入类型"/>
                </el-form-item>
                
                <el-form-item label="用户名" prop="deptId">
                    <el-input v-model="form.user_name" placeholder="请输入用户名"/>
                </el-form-item>
                
                <el-form-item label="工时制度" prop="deptId">
                    <el-input v-model="form.work_hour_system" placeholder="请输入工时制度"/>
                </el-form-item>
                
                <div slot="footer" class="dialog-footer">
                    <el-button type="primary" @click="submitForm">确 定</el-button>
                    <el-button @click="cancel">取 消</el-button>
                </div>
            </el-form>
        </el-dialog>
    </div>
</template>

<script>

export default {
    name: "User",
    data() {
        return {
            tableData: [],
            // 遮罩层
            loading: false,
            // 选中数组
            ids: [],
            // 非单个禁用
            single: true,
            // 非多个禁用
            multiple: true,
            // 显示搜索条件
            showSearch: true,
            // 总条数
            total: 0,
            // 弹出层标题
            title: "",
            // 是否显示弹出层
            open: false,
            // 查询参数
            queryForm: {},
            // 表单参数
            form: {},
            // 表单校验
            rules: {
                
                id: [{required: false, trigger: "blur", message: "主键id",}],
                
                create_by: [{required: false, trigger: "blur", message: "创建者id",}],
                
                create_time: [{required: false, trigger: "blur", message: "创建时间",}],
                
                update_by: [{required: false, trigger: "blur", message: "修改者id",}],
                
                update_time: [{required: false, trigger: "blur", message: "修改时间",}],
                
                email: [{required: false, trigger: "blur", message: "邮箱",}],
                
                entry_date: [{required: false, trigger: "blur", message: "入职日期",}],
                
                id_card: [{required: false, trigger: "blur", message: "身份证号",}],
                
                id_card_type: [{required: false, trigger: "blur", message: "证件类型",}],
                
                no: [{required: false, trigger: "blur", message: "工号",}],
                
                org_id: [{required: false, trigger: "blur", message: "部门",}],
                
                password: [{required: false, trigger: "blur", message: "密码",}],
                
                phone: [{required: false, trigger: "blur", message: "手机号码",}],
                
                post_id: [{required: false, trigger: "blur", message: "职位",}],
                
                state: [{required: false, trigger: "blur", message: "状态",}],
                
                type: [{required: false, trigger: "blur", message: "类型",}],
                
                user_name: [{required: false, trigger: "blur", message: "用户名",}],
                
                work_hour_system: [{required: false, trigger: "blur", message: "工时制度",}],
                
            }
        };
    },
    created() {
        this.init();
    },
    methods: {
        async init() {
            let response = await this.$getjson(WorkerApi, this.queryForm);
            if (response.data.code != 1) {
                this.$message.error(response.data.data);
                return
            }
            this.tableData = response.data
            this.total = response.total
        },
        query() {
            this.queryForm.page = 1;
            this.init();
        },
        queryReset() {
            // todo
        },
        /** 新增按钮操作 */
        handleAdd() {
            this.form = null;
            this.open = true;
            this.title = "新增";
        },
        /** 修改按钮操作 */
        handleUpdate(row) {
            this.form = row;
            this.open = true;
            this.title = "修改";
        },
        /** 取消 */
        cancel() {
            this.form = null;
            this.open = true;
            this.title = "新增";
        },
        /** 提交 -- 新增或者修改 */
        submitForm() {
            this.$refs["form"].validate(valid => {
                if (valid) {
                    if (this.form.id == null) {
                        this.postjosn(this.form)
                        this.$message.success("修改成功");
                    } else {
                        this.putjson(this.form)
                        this.$message.success("修改成功");
                    }
                    // this.this.ppjson(this.form)
                    this.open = false;
                    this.init();
                }
            });
        },
        // 批量删除或者单个删除
        handleDelete(row) {
            this.deletejson(url, row.id)
        },
    }
};
</script>