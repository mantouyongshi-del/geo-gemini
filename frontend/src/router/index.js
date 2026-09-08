import { createRouter, createWebHashHistory } from 'vue-router';
import HomeLanding from '../views/HomeLanding.vue';
import AiReport from '../views/AiReport.vue';
import DiagnosticConsole from '../views/DiagnosticConsole.vue';
import DiagnosticReport from '../views/DiagnosticReport.vue';

const routes = [
  {
    path: '/',
    name: 'HomeLanding',
    component: HomeLanding,
    meta: { title: '蜉蝣小宝 · GEO 新一代生成式 AI 搜索引擎商业认知与拓客中枢' }
  },
  {
    path: '/console',
    name: 'ConsoleAlias',
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
    path: '/diagnostic',
    name: 'DiagnosticConsole',
    component: DiagnosticConsole,
    meta: { title: '蜉蝣小宝 · 企业 AI 可见度售前体检工作台' }
  },
  {
    path: '/diagnostic_report',
    name: 'DiagnosticReport',
    component: DiagnosticReport,
    meta: { title: '蜉蝣小宝 · 企业 AI 搜索引擎可见度诊断体检书' }
  },
  {
    path: '/diagnostic/report/:code?',
    name: 'DiagnosticReportParam',
    component: DiagnosticReport,
    meta: { title: '蜉蝣小宝 · 企业 AI 搜索引擎可见度诊断体检书' }
  }
];

const router = createRouter({
  history: createWebHashHistory(),
  routes
});

router.beforeEach((to, from, next) => {
  if (to.meta.title) {
    document.title = to.meta.title;
  }
  next();
});

export default router;
