
export const ATTENDANCE_API = '/api/attendance/';
export const ATTENDANCE_CRATE_API = "/api/attendance/crate";
export const ATTENDANCE_PAGE_API = "/api/attendance/getPage";
export const ATTENDANCE_UPDATE_API = "/api/attendance/update";
export const ATTENDANCE_DELETE_API = "/api/attendance/delete";
export const ATTENDANCE_DELETE_BATCH_API = "/api/attendance/deleteBatch";

export const CALENDAR_API = '/api/calendar/';
export const CALENDAR_CRATE_API = "/api/calendar/crate";
export const CALENDAR_PAGE_API = "/api/calendar/getPage";
export const CALENDAR_UPDATE_API = "/api/calendar/update";
export const CALENDAR_DELETE_API = "/api/calendar/delete";
export const CALENDAR_DELETE_BATCH_API = "/api/calendar/deleteBatch";

export const COMPANY_API = '/api/company/';
export const COMPANY_CRATE_API = "/api/company/crate";
export const COMPANY_PAGE_API = "/api/company/getPage";
export const COMPANY_UPDATE_API = "/api/company/update";
export const COMPANY_DELETE_API = "/api/company/delete";
export const COMPANY_DELETE_BATCH_API = "/api/company/deleteBatch";

export const ENUM_API = '/api/enum/';
export const ENUM_CRATE_API = "/api/enum/crate";
export const ENUM_PAGE_API = "/api/enum/getPage";
export const ENUM_UPDATE_API = "/api/enum/update";
export const ENUM_DELETE_API = "/api/enum/delete";
export const ENUM_DELETE_BATCH_API = "/api/enum/deleteBatch";

export const FORM_API = '/api/form/';
export const FORM_CRATE_API = "/api/form/crate";
export const FORM_PAGE_API = "/api/form/getPage";
export const FORM_UPDATE_API = "/api/form/update";
export const FORM_DELETE_API = "/api/form/delete";
export const FORM_DELETE_BATCH_API = "/api/form/deleteBatch";

export const FORM_ITEM_API = '/api/formItem/';
export const FORM_ITEM_CRATE_API = "/api/formItem/crate";
export const FORM_ITEM_PAGE_API = "/api/formItem/getPage";
export const FORM_ITEM_UPDATE_API = "/api/formItem/update";
export const FORM_ITEM_DELETE_API = "/api/formItem/delete";
export const FORM_ITEM_DELETE_BATCH_API = "/api/formItem/deleteBatch";

export const MEMO_API = '/api/memo/';
export const MEMO_CRATE_API = "/api/memo/crate";
export const MEMO_PAGE_API = "/api/memo/getPage";
export const MEMO_UPDATE_API = "/api/memo/update";
export const MEMO_DELETE_API = "/api/memo/delete";
export const MEMO_DELETE_BATCH_API = "/api/memo/deleteBatch";

export const ORGANIZATION_API = '/api/organization/';
export const ORGANIZATION_CRATE_API = "/api/organization/crate";
export const ORGANIZATION_PAGE_API = "/api/organization/getPage";
export const ORGANIZATION_UPDATE_API = "/api/organization/update";
export const ORGANIZATION_DELETE_API = "/api/organization/delete";
export const ORGANIZATION_DELETE_BATCH_API = "/api/organization/deleteBatch";

export const ORGANIZATION_TYPE_API = '/api/organizationType/';
export const ORGANIZATION_TYPE_CRATE_API = "/api/organizationType/crate";
export const ORGANIZATION_TYPE_PAGE_API = "/api/organizationType/getPage";
export const ORGANIZATION_TYPE_UPDATE_API = "/api/organizationType/update";
export const ORGANIZATION_TYPE_DELETE_API = "/api/organizationType/delete";
export const ORGANIZATION_TYPE_DELETE_BATCH_API = "/api/organizationType/deleteBatch";

export const PERFORMANCE_API = '/api/performance/';
export const PERFORMANCE_CRATE_API = "/api/performance/crate";
export const PERFORMANCE_PAGE_API = "/api/performance/getPage";
export const PERFORMANCE_UPDATE_API = "/api/performance/update";
export const PERFORMANCE_DELETE_API = "/api/performance/delete";
export const PERFORMANCE_DELETE_BATCH_API = "/api/performance/deleteBatch";

export const PERFORMANCE_INFO_API = '/api/performanceInfo/';
export const PERFORMANCE_INFO_CRATE_API = "/api/performanceInfo/crate";
export const PERFORMANCE_INFO_PAGE_API = "/api/performanceInfo/getPage";
export const PERFORMANCE_INFO_UPDATE_API = "/api/performanceInfo/update";
export const PERFORMANCE_INFO_DELETE_API = "/api/performanceInfo/delete";
export const PERFORMANCE_INFO_DELETE_BATCH_API = "/api/performanceInfo/deleteBatch";

export const POST_API = '/api/post/';
export const POST_CRATE_API = "/api/post/crate";
export const POST_PAGE_API = "/api/post/getPage";
export const POST_UPDATE_API = "/api/post/update";
export const POST_DELETE_API = "/api/post/delete";
export const POST_DELETE_BATCH_API = "/api/post/deleteBatch";

export const POST_LEVEL_API = '/api/postLevel/';
export const POST_LEVEL_CRATE_API = "/api/postLevel/crate";
export const POST_LEVEL_PAGE_API = "/api/postLevel/getPage";
export const POST_LEVEL_UPDATE_API = "/api/postLevel/update";
export const POST_LEVEL_DELETE_API = "/api/postLevel/delete";
export const POST_LEVEL_DELETE_BATCH_API = "/api/postLevel/deleteBatch";

export const USER_API = '/api/user/';
export const USER_CRATE_API = "/api/user/crate";
export const USER_PAGE_API = "/api/user/getPage";
export const USER_UPDATE_API = "/api/user/update";
export const USER_DELETE_API = "/api/user/delete";
export const USER_DELETE_BATCH_API = "/api/user/deleteBatch";

export const USER_ROLE_API = '/api/userRole/';
export const USER_ROLE_CRATE_API = "/api/userRole/crate";
export const USER_ROLE_PAGE_API = "/api/userRole/getPage";
export const USER_ROLE_UPDATE_API = "/api/userRole/update";
export const USER_ROLE_DELETE_API = "/api/userRole/delete";
export const USER_ROLE_DELETE_BATCH_API = "/api/userRole/deleteBatch";



export const ATTENDANCE_URL = '/Attendance';

export const CALENDAR_URL = '/Calendar';

export const COMPANY_URL = '/Company';

export const ENUM_URL = '/Enum';

export const FORM_URL = '/Form';

export const FORM_ITEM_URL = '/FormItem';

export const MEMO_URL = '/Memo';

export const ORGANIZATION_URL = '/Organization';

export const ORGANIZATION_TYPE_URL = '/OrganizationType';

export const PERFORMANCE_URL = '/Performance';

export const PERFORMANCE_INFO_URL = '/PerformanceInfo';

export const POST_URL = '/Post';

export const POST_LEVEL_URL = '/PostLevel';

export const USER_URL = '/User';

export const USER_ROLE_URL = '/UserRole';


const routes = [
    
    {
        path: ATTENDANCE_URL,
        component: () => import('@/views/Attendance'),
    },
    
    {
        path: CALENDAR_URL,
        component: () => import('@/views/Calendar'),
    },
    
    {
        path: COMPANY_URL,
        component: () => import('@/views/Company'),
    },
    
    {
        path: ENUM_URL,
        component: () => import('@/views/Enum'),
    },
    
    {
        path: FORM_URL,
        component: () => import('@/views/Form'),
    },
    
    {
        path: FORM_ITEM_URL,
        component: () => import('@/views/FormItem'),
    },
    
    {
        path: MEMO_URL,
        component: () => import('@/views/Memo'),
    },
    
    {
        path: ORGANIZATION_URL,
        component: () => import('@/views/Organization'),
    },
    
    {
        path: ORGANIZATION_TYPE_URL,
        component: () => import('@/views/OrganizationType'),
    },
    
    {
        path: PERFORMANCE_URL,
        component: () => import('@/views/Performance'),
    },
    
    {
        path: PERFORMANCE_INFO_URL,
        component: () => import('@/views/PerformanceInfo'),
    },
    
    {
        path: POST_URL,
        component: () => import('@/views/Post'),
    },
    
    {
        path: POST_LEVEL_URL,
        component: () => import('@/views/PostLevel'),
    },
    
    {
        path: USER_URL,
        component: () => import('@/views/User'),
    },
    
    {
        path: USER_ROLE_URL,
        component: () => import('@/views/UserRole'),
    },
    
];
export default routes;