const menu_list = [

    {

        title: '驾驶舱',

        pid: '1',

        url: '/dashboard',

        id: 'dashboard',

        icon: 'liangrongkehufengxianguanli1'

    },

    {

        key: '/liangrong-risk',

        pid: '2',

        icon: 'liangrongfengxianjiankong',

        marginRight: '8px',

        width: '1.2em',

        height: '1.2em',

        title: '两融风险监控',

        id: 'fina_secu_risk_monitor',

        children: [

            {

                title: '宏观观测指标',

                url: '/liangrong-risk/macro-indicators',

                id: 'fina_secu_risk_macro_indicators',

                icon: 'dian',

            },

            {

                title: '合约监控',

                url: '/liangrong-risk/contract-monitor',

                id: 'fina_secu_risk_contract_monitor',

                icon: 'dian',

            },

            {

                title: '单一证券占总股本比例',

                url: '/liangrong-risk/single_sec_capitalization_ratio',

                id: 'fina_secu_risk_single_sec_capitalization_ratio',

                icon: 'dian',

            },

            {

                title: '融资融券全市场数据',

                url: '/liangrong-risk/market-data',

                id: 'fina_secu_risk_market_data',

                icon: 'dian',

            },

            {

                title: '融资融券业务风险指标',

                url: '/liangrong-risk/business_risk_indicator',

                id: 'fina_secu_risk_business_risk_indicator',

                icon: 'dian',

            },

            {

                title: '盘中大额买入监控',

                url: '/liangrong-risk/large-intraday-purchase',

                id: 'fina_secu_risk_xcb_monitor',

                icon: 'dian',

            },

        ]

    },

    {

        key: '/liangrong-cus',

        pid: '2',

        icon: 'liangrongkehufengxianguanli1',

        title: '两融客户风险管理',

        id: 'fina_secu_cus_risk',

        children: [

            {

                title: '客户画像',

                url: '/liangrong-cus/customer',

                id: 'fina_secu_cus_list',

                icon: 'dian',

            },

            {

                title: '净空头客户',

                url: '/liangrong-cus/short-customer',

                id: 'fina_secu_short_cus_list',

                icon: 'dian',

            },

            {

                title: '数据分析-客户可视化分析',

                url: '/liangrong-cus/cus-visualization',

                id: 'fina_secu_cus_visual',

                icon: 'dian',

            },

            {

                title: '专项券源合约监控',

                url: '/liangrong-cus/specific-sec-monitor',

                id: 'fina_secu_specific_sec_monitor',

                icon: 'dian',

            },

            {

                title: '证券异动',

                url: '/liangrong-cus/sec-change',

                id: 'fina_secu_sec_change',

                icon: 'dian',

            },

            {

                title: '注册制持仓客户',

                url: '/liangrong-cus/registered-customer',

                id: 'fina_secu_registered_cus_list',

                icon: 'dian',

            },

            {

                title: '负债客户信息监控',

                url: '/liangrong-cus/debt-customer-monitor',

                id: 'fina_secu_debt_cus_monitor',

                icon: 'dian',

            },

            {

                title: '重点客户名单',

                url: '/liangrong-cus/critical-customer',

                id: 'fina_secu_critical_cus_list',

                icon: 'dian',

            },

            {

                title: '客户风险等级设置',

                url: '/liangrong-cus/cus-risk-level-config',

                id: 'fina_secu_cus_risk_level_config',

                icon: 'dian',

            },

            // {

            //   title: '客户评分规则设置',

            //   url: '/liangrong-cus/cus-score-rule',

            //   id: 'fina_secu_cus_risk_level_config',

            //   icon: 'dian',

            // },

        ]

    },

    {

        key: '/liangrong',

        pid: '2',

        icon: 'danbaopinfengkong1',

        title: '担保品风控',

        id: 'collateral_risk',

        children: [

            {

                title: '证券列表',

                url: '/liangrong/securities',

                id: 'fina_secu_securities',

                icon: 'dian',

            },

            {

                title: '担保品评分',

                url: '/liangrong/search',

                id: 'fina_secu_search',

                icon: 'dian',

            },

            {

                title: '折算率管理',

                url: '/liangrong/manage',

                id: 'fina_secu_manage',

                icon: 'dian',

            },

            {

                title: '折算率定调',

                url: '/liangrong/suggest-new',

                id: 'fina_secu_suggest_new',

                icon: 'dian',

            },

            {

                title: '证券名单导入',

                url: '/liangrong/sec-import',

                id: 'fina_secu_sec_import',

                icon: 'dian',

            },

            {

                title: '成分股列表',

                url: '/liangrong/constituent-stock',

                id: 'fina_secu_constituent_stock',

                icon: 'dian',

            }

        ]

    },

    {

        key: '/system-configuration',


        pid: '2',

        title: '证券评分模型配置',

        id: 'collateral_model',

        icon: 'zhengquanpingfenmoxingpeizhi1',

        children: [

            {

                title: '方案配置',

                url: '/system-configuration/scenario',

                id: 'scenario_config',

                icon: 'dian'

            },

            {

                title: '评分项配置',

                url: '/system-configuration/score-entry',

                id: 'score_config',

                icon: 'dian'

            },

            {

                title: '指标池管理',

                url: '/system-configuration/metric-pool',

                id: 'metric_config',

                icon: 'dian'

            },

        ]

    },

    {

        key: '/ainew',

        pid: '2',

        icon: 'zhinengyuqing',

        title: '智能舆情',

        id: 'ai_news',

        children: [

            {

                title: '舆情首页',

                url: '/ainew/home',

                id: 'news_home',

                icon: 'dian'

            },

            {

                title: '公司舆情',

                url: '/ainew/companylist',

                id: 'company_list',

                icon: 'dian'

            },

            {

                title: '舆情列表',

                url: '/ainew/newlist',

                id: 'news_list',

                icon: 'dian'

            }

        ]

    },

    {

        key: '/test',

        pid: '2',

        icon: 'liangrongfengxianjiankong',

        title: '压力测试',

        id: 'stress_test',

        children: [

            {

                title: '压测任务列表',

                url: '/test/home',

                id: 'test_home',

                icon: 'dian',

            },

            // {

            //   title: '压测客户范围',

            //   url: '/test/customer-range',

            //   id: 'test_customer_range',

            //   icon: 'dian',

            // },

            // {

            //   title: '压测情景设置',

            //   url: '/test/home/detail',

            //   id: 'test_detail',

            //   icon: 'dian',

            // },

            // {

            //   title: '压测结果输出',

            //   url: '/test/home/result',

            //   id: 'test_result',

            //   icon: 'dian',

            // },

        ]

    },

    {

        title: '舆情首页',

        url: '/pledge-risk/ainew/home',

        pid: '3',

        id: 'pledge_news_home',

        icon: 'zhinengyuqing'

    },


    {

        key: '/pledge-risk',

        pid: '3',

        icon: 'liangrongfengxianjiankong',

        title: '股票质押舆情',

        id: 'pledge_ai_news',

        children: [

            {

                title: '证券风险分析',

                url: '/pledge-risk/companyrisk',

                id: 'company_risk',

                icon: 'dian'

            },

            {

                title: '质押标的评分',

                url: '/pledge-risk/ainew/companylist',

                id: 'pledge_company_list',

                icon: 'dian'

            },

            {

                title: '标的券舆情',

                url: '/pledge-risk/ainew/newlist',

                id: 'pledge_news_list',

                icon: 'dian'

            },

            {

                title: '融资人舆情',

                url: '/pledge-risk/ainew/financiernewlist',

                id: 'pledge_financier_news_list',

                icon: 'dian'

            }

        ]

    },

    {

        key: '/pledge',

        pid: '3',

        icon: 'xingzhuang',

        title: '系统管理',

        id: 'zhiya-config',

        children: [

            {

                title: '标的券关注池',

                url: '/pledge/sec-attention-pool',

                id: 'sec-attention-pool',

                icon: 'dian'

            },

            {

                title: '融资人关注池',

                url: '/pledge/financier-attention-pool',

                id: 'financier-attention-pool',

                icon: 'dian'

            },

            {

                title: '分组管理',

                url: '/pledge/ainew/group',

                id: 'pledge_tag_management',

                icon: 'dian'

            },

            {

                title: '方案配置',

                url: '/pledge/code-configuration/scenario',

                id: 'code_scenario_config',

                icon: 'dian'

            },

            {

                title: '评分项配置',

                url: '/pledge/code-configuration/score-entry',

                id: 'code_score_config',

                icon: 'dian'

            },

            {

                title: '指标池管理',

                url: '/pledge/code-configuration/metric-pool',

                id: 'code_metric_config',

                icon: 'dian'

            }

        ]

    },

    {

        title: '机构管理',

        pid: '4',

        url: '/power/department',

        id: 'department_manage',

        icon: 'jigoubianzhi'

    },

    {

        title: '用户管理',

        pid: '4',

        url: '/power/user',

        id: 'user_manage',

        icon: 'yonghu1'

    },

    {

        title: '角色权限管理',

        pid: '4',

        url: '/power/role',

        id: 'user_role_manage',

        icon: 'authority'

    },

    {

        title: '任务监控',

        pid: '4',

        url: '/monitor/task',

        id: 'task_monitor',

        icon: 'yonghu1'

    },

    {

        title: '事件监控',

        pid: '4',

        url: '/monitor/event',

        id: 'event_monitor',

        icon: 'authority'

    },

    {

        title: '个人中心',

        pid: '4',

        url: '/power/self',

        id: 'system_self',

        icon: 'yonghu1'

    },

]