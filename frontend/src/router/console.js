import { createRouter, createWebHashHistory } from 'vue-router';
import SalesConsole from '../views/SalesConsole.vue';
import DiagnosticReport from '../views/DiagnosticReport.vue';

const routes = [
  {
    path: '/',
    name: 'SalesConsole',
    component: SalesConsole,
    meta: { title: '蜉蝣小宝 · GEO 商业认知与销售演示工作台' }
  },
  {
    path: '/diagnostic',
    redirect: '/'
  },
  {
    path: '/leads',
    name: 'ConsoleLeads',
    component: SalesConsole,
    meta: { title: '蜉蝣小宝 · 官网获客线索池' }
  },
  {
    path: '/archive',
    name: 'ConsoleArchive',
    component: SalesConsole,
    meta: { title: '蜉蝣小宝 · 历史体检报告归档' }
  },
  {
    path: '/diagnostic_report',
    name: 'ConsoleDiagnosticReport',
    component: DiagnosticReport,
    meta: { title: '蜉蝣小宝 · 企业 AI 搜索引擎可见度诊断体检书' }
  },
  {
    path: '/diagnostic/report/:code?',
    name: 'ConsoleDiagnosticReportParam',
    component: DiagnosticReport,
    meta: { title: '蜉蝣小宝 · 企业 AI 搜索引擎可见度诊断体检书' }
  }
];

const consoleRouter = createRouter({
  history: createWebHashHistory(),
  routes
});

consoleRouter.beforeEach((to, from, next) => {
  if (to.meta.title) {
    document.title = to.meta.title;
  }
  next();
});

export default consoleRouter;
