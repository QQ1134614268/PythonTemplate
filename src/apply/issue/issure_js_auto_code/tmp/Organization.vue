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
            
            <el-form-item label="工作地点" prop="deptId">
                <el-input v-model="queryForm.area" placeholder="请输入工作地点"/>
            </el-form-item>
            
            <el-form-item label="工作城市" prop="deptId">
                <el-input v-model="queryForm.city" placeholder="请输入工作城市"/>
            </el-form-item>
            
            <el-form-item label="组织描述" prop="deptId">
                <el-input v-model="queryForm.description" placeholder="请输入组织描述"/>
            </el-form-item>
            
            <el-form-item label="编制人数" prop="deptId">
                <el-input v-model="queryForm.headcount" placeholder="请输入编制人数"/>
            </el-form-item>
            
            <el-form-item label="负责人ID" prop="deptId">
                <el-input v-model="queryForm.leaderId" placeholder="请输入负责人ID"/>
            </el-form-item>
            
            <el-form-item label="组织编号" prop="deptId">
                <el-input v-model="queryForm.orgCode" placeholder="请输入组织编号"/>
            </el-form-item>
            
            <el-form-item label="组织名称" prop="deptId">
                <el-input v-model="queryForm.orgName" placeholder="请输入组织名称"/>
            </el-form-item>
            
            <el-form-item label="上级组织编码" prop="deptId">
                <el-input v-model="queryForm.parentCode" placeholder="请输入上级组织编码"/>
            </el-form-item>
            
            <el-form-item label="组织简称" prop="deptId">
                <el-input v-model="queryForm.shortName" placeholder="请输入组织简称"/>
            </el-form-item>
            
            <el-form-item label="组织状态" prop="deptId">
                <el-input v-model="queryForm.state" placeholder="请输入组织状态"/>
            </el-form-item>
            
            <el-form-item label="组织类型" prop="deptId">
                <el-input v-model="queryForm.type" placeholder="请输入组织类型"/>
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
            
            <el-table-column label="工作地点" prop="area" width="55" align="center"></el-table-column>
            
            <el-table-column label="工作城市" prop="city" width="55" align="center"></el-table-column>
            
            <el-table-column label="组织描述" prop="description" width="55" align="center"></el-table-column>
            
            <el-table-column label="编制人数" prop="headcount" width="55" align="center"></el-table-column>
            
            <el-table-column label="负责人ID" prop="leaderId" width="55" align="center"></el-table-column>
            
            <el-table-column label="组织编号" prop="orgCode" width="55" align="center"></el-table-column>
            
            <el-table-column label="组织名称" prop="orgName" width="55" align="center"></el-table-column>
            
            <el-table-column label="上级组织编码" prop="parentCode" width="55" align="center"></el-table-column>
            
            <el-table-column label="组织简称" prop="shortName" width="55" align="center"></el-table-column>
            
            <el-table-column label="组织状态" prop="state" width="55" align="center"></el-table-column>
            
            <el-table-column label="组织类型" prop="type" width="55" align="center"></el-table-column>
            
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
                
                <el-form-item label="工作地点" prop="deptId">
                    <el-input v-model="form.area" placeholder="请输入工作地点"/>
                </el-form-item>
                
                <el-form-item label="工作城市" prop="deptId">
                    <el-input v-model="form.city" placeholder="请输入工作城市"/>
                </el-form-item>
                
                <el-form-item label="组织描述" prop="deptId">
                    <el-input v-model="form.description" placeholder="请输入组织描述"/>
                </el-form-item>
                
                <el-form-item label="编制人数" prop="deptId">
                    <el-input v-model="form.headcount" placeholder="请输入编制人数"/>
                </el-form-item>
                
                <el-form-item label="负责人ID" prop="deptId">
                    <el-input v-model="form.leaderId" placeholder="请输入负责人ID"/>
                </el-form-item>
                
                <el-form-item label="组织编号" prop="deptId">
                    <el-input v-model="form.orgCode" placeholder="请输入组织编号"/>
                </el-form-item>
                
                <el-form-item label="组织名称" prop="deptId">
                    <el-input v-model="form.orgName" placeholder="请输入组织名称"/>
                </el-form-item>
                
                <el-form-item label="上级组织编码" prop="deptId">
                    <el-input v-model="form.parentCode" placeholder="请输入上级组织编码"/>
                </el-form-item>
                
                <el-form-item label="组织简称" prop="deptId">
                    <el-input v-model="form.shortName" placeholder="请输入组织简称"/>
                </el-form-item>
                
                <el-form-item label="组织状态" prop="deptId">
                    <el-input v-model="form.state" placeholder="请输入组织状态"/>
                </el-form-item>
                
                <el-form-item label="组织类型" prop="deptId">
                    <el-input v-model="form.type" placeholder="请输入组织类型"/>
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
import { ORGANIZATION_CRATE_API, ORGANIZATION_PAGE_API, ORGANIZATION_UPDATE_API, ORGANIZATION_DELETE_API, ORGANIZATION_DELETE_BATCH_API } from "@/api/api";

export default {
    name: "Organization",
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
                
                area: [{required: false, trigger: "blur", message: "工作地点",}],
                
                city: [{required: false, trigger: "blur", message: "工作城市",}],
                
                description: [{required: false, trigger: "blur", message: "组织描述",}],
                
                headcount: [{required: false, trigger: "blur", message: "编制人数",}],
                
                leaderId: [{required: false, trigger: "blur", message: "负责人ID",}],
                
                orgCode: [{required: false, trigger: "blur", message: "组织编号",}],
                
                orgName: [{required: false, trigger: "blur", message: "组织名称",}],
                
                parentCode: [{required: false, trigger: "blur", message: "上级组织编码",}],
                
                shortName: [{required: false, trigger: "blur", message: "组织简称",}],
                
                state: [{required: false, trigger: "blur", message: "组织状态",}],
                
                type: [{required: false, trigger: "blur", message: "组织类型",}],
                
            }
        };
    },
    created() {
        this.init();
    },
    methods: {
        async init() {
            let response = await getJson2(ORGANIZATION_PAGE_API, this.queryForm);
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
                        postJson2(ORGANIZATION_CRATE_API, this.form);
                        this.$message.success("修改成功");
                    } else {
                        postJson2(ORGANIZATION_UPDATE_API, this.form);
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
            postJson2(ORGANIZATION_DELETE_API, row.id);
        },
    }
};
</script>