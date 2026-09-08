import { createRouter, createWebHashHistory } from 'vue-router';
import DiagnosticConsole from '../views/DiagnosticConsole.vue';
import DiagnosticReport from '../views/DiagnosticReport.vue';
import AiReport from '../views/AiReport.vue';

const routes = [
  {
    path: '/',
    name: 'DiagnosticConsole',
    component: DiagnosticConsole,
    meta: { title: '蜉蝣小宝 · 企业 AI 可见度售前体检工作台' }
  },
  {
    path: '/diagnostic',
    name: 'DiagnosticAlias',
    component: DiagnosticConsole,
    meta: { title: '蜉蝣小宝 · 企业 AI 可见度售前体检工作台' }
  },
  {
    path: '/ai_report',
    name: 'AiReport',
    component: AiReport,
    meta: { title: '蜉蝣小宝 · GEO 智能搜索排名与推荐优化看板' }
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
