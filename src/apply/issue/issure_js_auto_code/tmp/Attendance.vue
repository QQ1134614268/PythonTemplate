<template>
    <div class="app-container">
        <el-form :model="queryForm" ref="queryForm" size="small" :inline="true" v-show="showSearch"
                 label-width="68px">
            
            <el-form-item label="主键id" prop="deptId">
                <el-input v-model="queryForm.id" placeholder="请输入主键id"/>
            </el-form-item>
            
            <el-form-item label="创建者id" prop="deptId">
                <el-input v-model="queryForm.createBy" placeholder="请输入创建者id"/>
            </el-form-item>
            
            <el-form-item label="创建时间" prop="deptId">
                <el-input v-model="queryForm.createTime" placeholder="请输入创建时间"/>
            </el-form-item>
            
            <el-form-item label="修改者id" prop="deptId">
                <el-input v-model="queryForm.updateBy" placeholder="请输入修改者id"/>
            </el-form-item>
            
            <el-form-item label="修改时间" prop="deptId">
                <el-input v-model="queryForm.updateTime" placeholder="请输入修改时间"/>
            </el-form-item>
            
            <el-form-item label="下班打卡时间" prop="deptId">
                <el-input v-model="queryForm.offTime" placeholder="请输入下班打卡时间"/>
            </el-form-item>
            
            <el-form-item label="上班打卡时间" prop="deptId">
                <el-input v-model="queryForm.onTime" placeholder="请输入上班打卡时间"/>
            </el-form-item>
            
            <el-form-item label="员工id" prop="deptId">
                <el-input v-model="queryForm.userId" placeholder="请输入员工id"/>
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
        <el-table v-loading="loading" :data="tableData">
            
            <el-table-column label="主键id" prop="id" width="55" align="center"></el-table-column>
            
            <el-table-column label="创建者id" prop="createBy" width="55" align="center"></el-table-column>
            
            <el-table-column label="创建时间" prop="createTime" width="55" align="center"></el-table-column>
            
            <el-table-column label="修改者id" prop="updateBy" width="55" align="center"></el-table-column>
            
            <el-table-column label="修改时间" prop="updateTime" width="55" align="center"></el-table-column>
            
            <el-table-column label="下班打卡时间" prop="offTime" width="55" align="center"></el-table-column>
            
            <el-table-column label="上班打卡时间" prop="onTime" width="55" align="center"></el-table-column>
            
            <el-table-column label="员工id" prop="userId" width="55" align="center"></el-table-column>
            
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
        <el-pagination @current-change="init" :current-page="page" :total="total"></el-pagination>

        <el-dialog :title="title" :visible.sync="open" width="500px" append-to-body>
            <el-form ref="form" :model="form" :rules="rules" label-width="80px">
                
                <el-form-item label="主键id" prop="deptId">
                    <el-input v-model="form.id" placeholder="请输入主键id"/>
                </el-form-item>
                
                <el-form-item label="创建者id" prop="deptId">
                    <el-input v-model="form.createBy" placeholder="请输入创建者id"/>
                </el-form-item>
                
                <el-form-item label="创建时间" prop="deptId">
                    <el-input v-model="form.createTime" placeholder="请输入创建时间"/>
                </el-form-item>
                
                <el-form-item label="修改者id" prop="deptId">
                    <el-input v-model="form.updateBy" placeholder="请输入修改者id"/>
                </el-form-item>
                
                <el-form-item label="修改时间" prop="deptId">
                    <el-input v-model="form.updateTime" placeholder="请输入修改时间"/>
                </el-form-item>
                
                <el-form-item label="下班打卡时间" prop="deptId">
                    <el-input v-model="form.offTime" placeholder="请输入下班打卡时间"/>
                </el-form-item>
                
                <el-form-item label="上班打卡时间" prop="deptId">
                    <el-input v-model="form.onTime" placeholder="请输入上班打卡时间"/>
                </el-form-item>
                
                <el-form-item label="员工id" prop="deptId">
                    <el-input v-model="form.userId" placeholder="请输入员工id"/>
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
import {postJson2, getJson2} from "@/api/util";
import { ATTENDANCE_CRATE_API, ATTENDANCE_PAGE_API, ATTENDANCE_UPDATE_API, ATTENDANCE_DELETE_API, ATTENDANCE_DELETE_BATCH_API } from "@/api/api";

export default {
    name: "Attendance",
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
            page: 1,
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
                
                createBy: [{required: false, trigger: "blur", message: "创建者id",}],
                
                createTime: [{required: false, trigger: "blur", message: "创建时间",}],
                
                updateBy: [{required: false, trigger: "blur", message: "修改者id",}],
                
                updateTime: [{required: false, trigger: "blur", message: "修改时间",}],
                
                offTime: [{required: false, trigger: "blur", message: "下班打卡时间",}],
                
                onTime: [{required: false, trigger: "blur", message: "上班打卡时间",}],
                
                userId: [{required: false, trigger: "blur", message: "员工id",}],
                
            }
        };
    },
    created() {
        this.init();
    },
    methods: {
        async init() {
            let response = await getJson2(ATTENDANCE_PAGE_API, this.queryForm);
            if (response.data.code != 1) {
                this.$message.error(response.data.data);
                return
            }
            this.tableData = response.data.data
            this.total = response.data.total
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
            this.form = {};
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
            this.form = {};
            this.open = true;
            this.title = "新增";
        },
        /** 提交 -- 新增或者修改 */
        submitForm() {
            this.$refs["form"].validate(valid => {
                if (valid) {
                    if (this.form.id == null) {
                        postJson2(ATTENDANCE_CRATE_API, this.form);
                        this.$message.success("修改成功");
                    } else {
                        postJson2(ATTENDANCE_UPDATE_API, this.form);
                        this.$message.success("修改成功");
                    }
                    // this.this.ppJson(_URL, this.form)
                    this.open = false;
                    this.init();
                }
            });
        },
        // 批量删除或者单个删除
        handleDelete(row) {
            postJson2(ATTENDANCE_DELETE_API, row.id);
        },
    }
};
</script>