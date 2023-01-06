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
            }
        ]
    },
]