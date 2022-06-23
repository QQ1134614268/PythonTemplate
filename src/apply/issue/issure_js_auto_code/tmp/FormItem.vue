<template>
  <div class="app-container">
    <el-form :model="queryForm" ref="queryForm" size="small" :inline="true" v-show="showSearch" label-width="68px">

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

      <el-form-item label="" prop="deptId">
        <el-input v-model="queryForm.characters" placeholder="请输入"/>
      </el-form-item>

      <el-form-item label="" prop="deptId">
        <el-input v-model="queryForm.checkItems" placeholder="请输入"/>
      </el-form-item>

      <el-form-item label="" prop="deptId">
        <el-input v-model="queryForm.date" placeholder="请输入"/>
      </el-form-item>

      <el-form-item label="" prop="deptId">
        <el-input v-model="queryForm.dateMax" placeholder="请输入"/>
      </el-form-item>

      <el-form-item label="" prop="deptId">
        <el-input v-model="queryForm.dateMin" placeholder="请输入"/>
      </el-form-item>

      <el-form-item label="" prop="deptId">
        <el-input v-model="queryForm.dateSection" placeholder="请输入"/>
      </el-form-item>

      <el-form-item label="" prop="deptId">
        <el-input v-model="queryForm.dateSectionBegin" placeholder="请输入"/>
      </el-form-item>

      <el-form-item label="" prop="deptId">
        <el-input v-model="queryForm.dateSectionEnd" placeholder="请输入"/>
      </el-form-item>

      <el-form-item label="" prop="deptId">
        <el-input v-model="queryForm.datetime" placeholder="请输入"/>
      </el-form-item>

      <el-form-item label="" prop="deptId">
        <el-input v-model="queryForm.datetimeMax" placeholder="请输入"/>
      </el-form-item>

      <el-form-item label="" prop="deptId">
        <el-input v-model="queryForm.datetimeMin" placeholder="请输入"/>
      </el-form-item>

      <el-form-item label="" prop="deptId">
        <el-input v-model="queryForm.fileItems" placeholder="请输入"/>
      </el-form-item>

      <el-form-item label="" prop="deptId">
        <el-input v-model="queryForm.info" placeholder="请输入"/>
      </el-form-item>

      <el-form-item label="" prop="deptId">
        <el-input v-model="queryForm.isRequired" placeholder="请输入"/>
      </el-form-item>

      <el-form-item label="" prop="deptId">
        <el-input v-model="queryForm.itemType" placeholder="请输入"/>
      </el-form-item>

      <el-form-item label="" prop="deptId">
        <el-input v-model="queryForm.memberItems" placeholder="请输入"/>
      </el-form-item>

      <el-form-item label="" prop="deptId">
        <el-input v-model="queryForm.money" placeholder="请输入"/>
      </el-form-item>

      <el-form-item label="" prop="deptId">
        <el-input v-model="queryForm.moneyUnit" placeholder="请输入"/>
      </el-form-item>

      <el-form-item label="" prop="deptId">
        <el-input v-model="queryForm.multiText" placeholder="请输入"/>
      </el-form-item>

      <el-form-item label="" prop="deptId">
        <el-input v-model="queryForm.num" placeholder="请输入"/>
      </el-form-item>

      <el-form-item label="" prop="deptId">
        <el-input v-model="queryForm.numMax" placeholder="请输入"/>
      </el-form-item>

      <el-form-item label="" prop="deptId">
        <el-input v-model="queryForm.numMin" placeholder="请输入"/>
      </el-form-item>

      <el-form-item label="" prop="deptId">
        <el-input v-model="queryForm.orgItems" placeholder="请输入"/>
      </el-form-item>

      <el-form-item label="" prop="deptId">
        <el-input v-model="queryForm.singleText" placeholder="请输入"/>
      </el-form-item>

      <el-form-item label="" prop="deptId">
        <el-input v-model="queryForm.sort" placeholder="请输入"/>
      </el-form-item>

      <el-form-item label="" prop="deptId">
        <el-input v-model="queryForm.timeSection" placeholder="请输入"/>
      </el-form-item>

      <el-form-item label="" prop="deptId">
        <el-input v-model="queryForm.timeSectionBegin" placeholder="请输入"/>
      </el-form-item>

      <el-form-item label="" prop="deptId">
        <el-input v-model="queryForm.timeSectionEnd" placeholder="请输入"/>
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

      <el-table-column label="" prop="characters" width="55" align="center"></el-table-column>

      <el-table-column label="" prop="checkItems" width="55" align="center"></el-table-column>

      <el-table-column label="" prop="date" width="55" align="center"></el-table-column>

      <el-table-column label="" prop="dateMax" width="55" align="center"></el-table-column>

      <el-table-column label="" prop="dateMin" width="55" align="center"></el-table-column>

      <el-table-column label="" prop="dateSection" width="55" align="center"></el-table-column>

      <el-table-column label="" prop="dateSectionBegin" width="55" align="center"></el-table-column>

      <el-table-column label="" prop="dateSectionEnd" width="55" align="center"></el-table-column>

      <el-table-column label="" prop="datetime" width="55" align="center"></el-table-column>

      <el-table-column label="" prop="datetimeMax" width="55" align="center"></el-table-column>

      <el-table-column label="" prop="datetimeMin" width="55" align="center"></el-table-column>

      <el-table-column label="" prop="fileItems" width="55" align="center"></el-table-column>

      <el-table-column label="" prop="info" width="55" align="center"></el-table-column>

      <el-table-column label="" prop="isRequired" width="55" align="center"></el-table-column>

      <el-table-column label="" prop="itemType" width="55" align="center"></el-table-column>

      <el-table-column label="" prop="memberItems" width="55" align="center"></el-table-column>

      <el-table-column label="" prop="money" width="55" align="center"></el-table-column>

      <el-table-column label="" prop="moneyUnit" width="55" align="center"></el-table-column>

      <el-table-column label="" prop="multiText" width="55" align="center"></el-table-column>

      <el-table-column label="" prop="num" width="55" align="center"></el-table-column>

      <el-table-column label="" prop="numMax" width="55" align="center"></el-table-column>

      <el-table-column label="" prop="numMin" width="55" align="center"></el-table-column>

      <el-table-column label="" prop="orgItems" width="55" align="center"></el-table-column>

      <el-table-column label="" prop="singleText" width="55" align="center"></el-table-column>

      <el-table-column label="" prop="sort" width="55" align="center"></el-table-column>

      <el-table-column label="" prop="timeSection" width="55" align="center"></el-table-column>

      <el-table-column label="" prop="timeSectionBegin" width="55" align="center"></el-table-column>

      <el-table-column label="" prop="timeSectionEnd" width="55" align="center"></el-table-column>

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

        <el-form-item label="" prop="deptId">
          <el-input v-model="form.characters" placeholder="请输入"/>
        </el-form-item>

        <el-form-item label="" prop="deptId">
          <el-input v-model="form.checkItems" placeholder="请输入"/>
        </el-form-item>

        <el-form-item label="" prop="deptId">
          <el-input v-model="form.date" placeholder="请输入"/>
        </el-form-item>

        <el-form-item label="" prop="deptId">
          <el-input v-model="form.dateMax" placeholder="请输入"/>
        </el-form-item>

        <el-form-item label="" prop="deptId">
          <el-input v-model="form.dateMin" placeholder="请输入"/>
        </el-form-item>

        <el-form-item label="" prop="deptId">
          <el-input v-model="form.dateSection" placeholder="请输入"/>
        </el-form-item>

        <el-form-item label="" prop="deptId">
          <el-input v-model="form.dateSectionBegin" placeholder="请输入"/>
        </el-form-item>

        <el-form-item label="" prop="deptId">
          <el-input v-model="form.dateSectionEnd" placeholder="请输入"/>
        </el-form-item>

        <el-form-item label="" prop="deptId">
          <el-input v-model="form.datetime" placeholder="请输入"/>
        </el-form-item>

        <el-form-item label="" prop="deptId">
          <el-input v-model="form.datetimeMax" placeholder="请输入"/>
        </el-form-item>

        <el-form-item label="" prop="deptId">
          <el-input v-model="form.datetimeMin" placeholder="请输入"/>
        </el-form-item>

        <el-form-item label="" prop="deptId">
          <el-input v-model="form.fileItems" placeholder="请输入"/>
        </el-form-item>

        <el-form-item label="" prop="deptId">
          <el-input v-model="form.info" placeholder="请输入"/>
        </el-form-item>

        <el-form-item label="" prop="deptId">
          <el-input v-model="form.isRequired" placeholder="请输入"/>
        </el-form-item>

        <el-form-item label="" prop="deptId">
          <el-input v-model="form.itemType" placeholder="请输入"/>
        </el-form-item>

        <el-form-item label="" prop="deptId">
          <el-input v-model="form.memberItems" placeholder="请输入"/>
        </el-form-item>

        <el-form-item label="" prop="deptId">
          <el-input v-model="form.money" placeholder="请输入"/>
        </el-form-item>

        <el-form-item label="" prop="deptId">
          <el-input v-model="form.moneyUnit" placeholder="请输入"/>
        </el-form-item>

        <el-form-item label="" prop="deptId">
          <el-input v-model="form.multiText" placeholder="请输入"/>
        </el-form-item>

        <el-form-item label="" prop="deptId">
          <el-input v-model="form.num" placeholder="请输入"/>
        </el-form-item>

        <el-form-item label="" prop="deptId">
          <el-input v-model="form.numMax" placeholder="请输入"/>
        </el-form-item>

        <el-form-item label="" prop="deptId">
          <el-input v-model="form.numMin" placeholder="请输入"/>
        </el-form-item>

        <el-form-item label="" prop="deptId">
          <el-input v-model="form.orgItems" placeholder="请输入"/>
        </el-form-item>

        <el-form-item label="" prop="deptId">
          <el-input v-model="form.singleText" placeholder="请输入"/>
        </el-form-item>

        <el-form-item label="" prop="deptId">
          <el-input v-model="form.sort" placeholder="请输入"/>
        </el-form-item>

        <el-form-item label="" prop="deptId">
          <el-input v-model="form.timeSection" placeholder="请输入"/>
        </el-form-item>

        <el-form-item label="" prop="deptId">
          <el-input v-model="form.timeSectionBegin" placeholder="请输入"/>
        </el-form-item>

        <el-form-item label="" prop="deptId">
          <el-input v-model="form.timeSectionEnd" placeholder="请输入"/>
        </el-form-item>

      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button type="primary" @click="submitForm">确 定</el-button>
        <el-button @click="cancel">取 消</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import {getJson2, postJson2} from "@/api/util";
import { FORM_ITEM_CREATE_API, FORM_ITEM_PAGE_API, FORM_ITEM_UPDATE_API, FORM_ITEM_DELETE_API, FORM_ITEM_DELETE_BATCH_API } from "@/api/api";

export default {
  name: "FormItem",
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
        characters: [{required: false, trigger: "blur", message: "",}],
        checkItems: [{required: false, trigger: "blur", message: "",}],
        date: [{required: false, trigger: "blur", message: "",}],
        dateMax: [{required: false, trigger: "blur", message: "",}],
        dateMin: [{required: false, trigger: "blur", message: "",}],
        dateSection: [{required: false, trigger: "blur", message: "",}],
        dateSectionBegin: [{required: false, trigger: "blur", message: "",}],
        dateSectionEnd: [{required: false, trigger: "blur", message: "",}],
        datetime: [{required: false, trigger: "blur", message: "",}],
        datetimeMax: [{required: false, trigger: "blur", message: "",}],
        datetimeMin: [{required: false, trigger: "blur", message: "",}],
        fileItems: [{required: false, trigger: "blur", message: "",}],
        info: [{required: false, trigger: "blur", message: "",}],
        isRequired: [{required: false, trigger: "blur", message: "",}],
        itemType: [{required: false, trigger: "blur", message: "",}],
        memberItems: [{required: false, trigger: "blur", message: "",}],
        money: [{required: false, trigger: "blur", message: "",}],
        moneyUnit: [{required: false, trigger: "blur", message: "",}],
        multiText: [{required: false, trigger: "blur", message: "",}],
        num: [{required: false, trigger: "blur", message: "",}],
        numMax: [{required: false, trigger: "blur", message: "",}],
        numMin: [{required: false, trigger: "blur", message: "",}],
        orgItems: [{required: false, trigger: "blur", message: "",}],
        singleText: [{required: false, trigger: "blur", message: "",}],
        sort: [{required: false, trigger: "blur", message: "",}],
        timeSection: [{required: false, trigger: "blur", message: "",}],
        timeSectionBegin: [{required: false, trigger: "blur", message: "",}],
        timeSectionEnd: [{required: false, trigger: "blur", message: "",}],
        
      }
    };
  },
  created() {
    this.init();
  },
  methods: {
    async init() {
      let response = await getJson2(FORM_ITEM_PAGE_API, this.queryForm);
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
    async submitForm() {
      this.$refs["form"].validate(async valid => {
        if (valid) {
          if (this.form.id == null) {
            await postJson2(FORM_ITEM_CREATE_API, this.form);
            this.$message.success("修改成功");
          } else {
            await postJson2(FORM_ITEM_UPDATE_API, this.form);
            this.$message.success("修改成功");
          }
          // this.this.ppJson(_URL, this.form)
          this.open = false;
          await this.init();
        }
      });
    },
    // 批量删除或者单个删除
    async handleDelete(row) {
      await postJson2(FORM_ITEM_DELETE_API, row.id);
      this.$message.success("删除成功");
      await this.init();
    },
  }
};
</script>