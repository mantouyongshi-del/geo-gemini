<template>
  <div class="console-container">
    <!-- 头部品牌条 -->
    <header class="console-header">
      <div class="header-inner">
        <div class="brand-badge">
          <span class="brand-logo-text">蜉蝣小宝</span>
          <span class="brand-tag">全国企业智能营销云 · 售前开单引擎</span>
        </div>
        <div class="header-nav">
          <router-link to="/ai_report" class="nav-link">📊 客户报表看板</router-link>
          <router-link to="/diagnostic" class="nav-link active">🎯 准客户 AI 可见度体检</router-link>
        </div>
      </div>
    </header>

    <main class="console-main">
      <div class="hero-section">
        <h1 class="hero-title">企业 AI 搜索引擎可见度 · 售前全网诊断台</h1>
        <p class="hero-sub">
          现场直连 <strong>豆包、DeepSeek、通义千问、腾讯元宝、百度搜索</strong>，出具震撼的《企业 AI 可见度体检报告》，用铁证向老板证明“潜在客户已被同行截流”！
        </p>
      </div>

      <div class="content-grid">
        <!-- 左侧: 诊断输入表单 -->
        <div class="card form-card">
          <h2 class="card-title">📝 录入准客户信息</h2>
          <form @submit.prevent="handleStartDiagnostic">
            <div class="form-group">
              <label class="form-label">准客户工商全称 (必填)</label>
              <input 
                v-model="form.target_company" 
                required 
                placeholder="例如: 杭州某某医疗美容门诊部 / 嘉兴市恒达门窗工程有限公司" 
                class="form-input" 
              />
            </div>

            <div class="form-row">
              <div class="form-group">
                <label class="form-label">品牌简称/常用名 (必填)</label>
                <input 
                  v-model="form.brand_name" 
                  required 
                  placeholder="例如: 华儿街少儿探索 / 恒达门窗" 
                  class="form-input" 
                />
              </div>
              <div class="form-group">
                <label class="form-label">所属行业领域 (必填)</label>
                <input 
                  v-model="form.industry" 
                  required 
                  placeholder="例如: 教育培训少儿科创 / 定制门窗" 
                  class="form-input" 
                />
              </div>
              <div class="form-group">
                <label class="form-label">展业城市/地区</label>
                <input 
                  v-model="form.city" 
                  placeholder="例如: 怀化 / 杭州 / 嘉兴" 
                  class="form-input" 
                />
              </div>
            </div>

            <!-- 快捷行业词模版 -->
            <div class="preset-templates">
              <span class="preset-label">实测案例快速填入:</span>
              <button 
                type="button" 
                v-for="tpl in industryTemplates" 
                :key="tpl.name" 
                class="preset-btn"
                @click="applyTemplate(tpl)"
              >
                {{ tpl.name }}
              </button>
            </div>

            <div class="form-group">
              <label class="form-label">核心测试搜索词 (提示词，每行一个)</label>
              <textarea 
                v-model="keywordsStr" 
                rows="4" 
                required
                placeholder="例如:&#10;嘉兴定制门窗推荐哪家&#10;嘉兴断桥铝系统门窗品牌排名&#10;嘉兴阳光房安装公司哪家口碑好"
                class="form-textarea"
              ></textarea>
              <span class="form-tip">建议输入 2~4 个带有地域或高频采购意向的实际搜索提问句</span>
            </div>

            <div class="agency-settings-box">
              <div class="box-title">🏢 加盟商授权署名设置 (打印及分享时展示)</div>
              <div class="form-row">
                <div class="form-group">
                  <label class="form-label">授权服务中心名称</label>
                  <input v-model="form.agency_name" class="form-input" />
                </div>
                <div class="form-group">
                  <label class="form-label">认证数字化顾问姓名</label>
                  <input v-model="form.consultant_name" class="form-input" />
                </div>
              </div>
            </div>

            <button type="submit" class="btn btn-submit" :disabled="isRunning">
              <span v-if="isRunning">📡 正在并发调度各大模型真实检索中... (预计 15 秒)</span>
              <span v-else>🚀 立即启动全网五大 AI 搜索引擎体检</span>
            </button>
          </form>
        </div>

        <!-- 右侧: 为什么能签单 & 最近体检历史 -->
        <div class="side-col">
          <!-- 签单销售打法指引卡 -->
          <div class="card pitch-card">
            <h3 class="pitch-title">💡 蜉蝣小宝 · 加盟商顾问签单秘籍</h3>
            <ul class="pitch-list">
              <li>
                <strong>① 现场打脸痛点：</strong> 给客户看体检分数（通常仅 10~18 分），用大红印章打破客户“在网上有知名度”的幻觉。
              </li>
              <li>
                <strong>② 竞品截流证据：</strong> 指着报告上的竞品名字问老板：“豆包和 DeepSeek 正在把你的准客户直接送给这家对手，你甘心吗？”
              </li>
              <li>
                <strong>③ 顺水推舟成交：</strong> 拿出蜉蝣小宝四维 GEO 解决方案，直接推 19,800 元/年 基础套餐，当场促单。
              </li>
            </ul>
          </div>

          <!-- 最近体检历史记录 -->
          <div class="card history-card">
            <div class="history-header">
              <h3 class="history-title">⏱️ 本地最近体检记录</h3>
              <button class="btn-refresh" @click="loadHistory">🔄 刷新</button>
            </div>

            <div class="history-list">
              <div v-for="h in recentHistory" :key="h.report_code" class="history-item">
                <div class="history-top">
                  <span class="h-company">{{ h.target_company }}</span>
                  <span class="h-score" :class="h.visibility_score < 30 ? 'score-danger' : 'score-ok'">
                    {{ h.visibility_score }} 分
                  </span>
                </div>
                <div class="history-bottom">
                  <span class="h-ind">{{ h.industry }}</span>
                  <router-link :to="`/diagnostic_report?code=${h.report_code}`" class="h-link">
                    查看诊断书 ➔
                  </router-link>
                </div>
              </div>
              <div v-if="recentHistory.length === 0" class="history-empty">
                暂无历史诊断记录，快为第一家客户体检吧！
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>

    <!-- 正在体检全屏雷达遮罩 -->
    <div v-if="isRunning" class="radar-backdrop">
      <div class="radar-box">
        <div class="radar-scanner"></div>
        <h3 class="radar-title">正在全网穿透探测中...</h3>
        <p class="radar-sub">已连接 字节豆包 · DeepSeek · 阿里千问 · 腾讯元宝 · 百度搜索</p>
        <div class="radar-status">正在深度提炼同行霸屏实体与 RAG 引文溯源...</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import geoApi from '../api/geo';

const router = useRouter();

const form = ref({
  target_company: '',
  brand_name: '',
  industry: '',
  city: '全国',
  agency_name: '蜉蝣小宝 · 华东授权运营中心',
  consultant_name: '金牌数字化顾问 张经理',
  consultant_phone: '138-0000-8888'
});

const keywordsStr = ref('');
const isRunning = ref(false);
const recentHistory = ref([]);

const industryTemplates = [
  {
    name: '🎯 华儿街少儿探索(怀化)',
    industry: '教育培训少儿科创',
    city: '怀化',
    company: '湖南暴雪文化科技有限公司',
    brand: '华儿街少儿探索',
    keywords: '怀化儿童学编程\n怀化少儿编程机构哪家好\n怀化机器人编程培训推荐'
  },
  {
    name: '门窗家居',
    industry: '高端定制门窗与阳光房',
    city: '嘉兴',
    company: '嘉兴市恒达门窗工程有限公司',
    brand: '恒达门窗',
    keywords: '嘉兴定制门窗哪家好\n嘉兴断桥铝系统门窗品牌排名\n嘉兴阳光房安装公司推荐'
  },
  {
    name: '医美诊所',
    industry: '专业医疗美容与轻医美',
    city: '杭州',
    company: '杭州臻美医疗美容门诊部',
    brand: '臻美医美',
    keywords: '杭州做热玛吉正规机构推荐\n杭州口碑好的轻医美诊所\n杭州微整注射医生排名'
  },
  {
    name: '财税法务',
    industry: '企业财税合规与法律顾问',
    city: '杭州',
    company: '浙江正信会计师事务所',
    brand: '正信财税',
    keywords: '杭州企业财税合规代理记账推荐\n浙江高新技术企业申报哪家专业\n杭州中小企业法律顾问收费'
  }
];

function applyTemplate(tpl) {
  form.value.target_company = tpl.company;
  form.value.brand_name = tpl.brand;
  form.value.industry = tpl.industry;
  form.value.city = tpl.city || '全国';
  keywordsStr.value = tpl.keywords;
}

async function handleStartDiagnostic() {
  const kws = keywordsStr.value.split('\n').map(k => k.trim()).filter(Boolean);
  if (!kws.length) {
    alert('请输入至少一个测试关键词');
    return;
  }

  isRunning.value = true;
  try {
    const res = await geoApi.runDiagnostic({
      target_company: form.value.target_company.trim(),
      brand_name: form.value.brand_name.trim(),
      industry: form.value.industry.trim(),
      city: form.value.city || '全国',
      keywords: kws,
      agency_name: form.value.agency_name,
      consultant_name: form.value.consultant_name,
      consultant_phone: form.value.consultant_phone
    });

    // 诊断完成，直接跳转至体检报告页面
    router.push({
      path: '/diagnostic_report',
      query: { code: res.data.report_code }
    });
  } catch (err) {
    alert('体检执行失败: ' + (err.response?.data?.detail || err.message));
  } finally {
    isRunning.value = false;
  }
}

async function loadHistory() {
  try {
    const res = await geoApi.getRecentDiagnostics();
    recentHistory.value = res.data;
  } catch (e) {
    console.error(e);
  }
}

onMounted(() => {
  loadHistory();
  // 默认填充一套经典门窗模板方便体验
  applyTemplate(industryTemplates[0]);
});
</script>

<style scoped>
.console-container {
  min-height: 100vh;
  background-color: #f1f5f9;
}

/* Header */
.console-header {
  background: #0f172a;
  color: #ffffff;
  padding: 1rem 2rem;
  border-bottom: 2px solid #6366f1;
}

.header-inner {
  max-width: 1300px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.brand-badge {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.brand-logo-text {
  font-size: 1.35rem;
  font-weight: 900;
  background: linear-gradient(135deg, #a5b4fc 0%, #6366f1 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  letter-spacing: 1px;
}

.brand-tag {
  background: #1e293b;
  border: 1px solid #334155;
  color: #cbd5e1;
  font-size: 0.75rem;
  padding: 0.2rem 0.6rem;
  border-radius: 4px;
}

.header-nav {
  display: flex;
  gap: 1rem;
}

.nav-link {
  color: #94a3b8;
  text-decoration: none;
  font-size: 0.875rem;
  font-weight: 600;
  padding: 0.4rem 0.8rem;
  border-radius: 6px;
  transition: all 0.15s;
}

.nav-link:hover, .nav-link.active {
  color: #ffffff;
  background: #1e293b;
}

/* Main */
.console-main {
  max-width: 1300px;
  margin: 2rem auto;
  padding: 0 1.5rem;
}

.hero-section {
  text-align: center;
  margin-bottom: 2rem;
}

.hero-title {
  font-size: 2rem;
  font-weight: 800;
  color: #0f172a;
}

.hero-sub {
  font-size: 1rem;
  color: #64748b;
  margin-top: 0.5rem;
  max-width: 760px;
  margin-left: auto;
  margin-right: auto;
}

/* Grid */
.content-grid {
  display: grid;
  grid-template-columns: 3fr 2fr;
  gap: 1.5rem;
}

@media (max-width: 900px) {
  .content-grid {
    grid-template-columns: 1fr;
  }
}

.card {
  background: #ffffff;
  border-radius: 12px;
  border: 1px solid #e2e8f0;
  padding: 1.5rem;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.03);
}

.card-title {
  font-size: 1.15rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 1.25rem;
}

/* Form */
.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
  margin-bottom: 1rem;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.form-label {
  font-size: 0.85rem;
  font-weight: 600;
  color: #334155;
}

.form-input, .form-textarea {
  padding: 0.6rem 0.85rem;
  border: 1px solid #cbd5e1;
  border-radius: 8px;
  font-size: 0.9rem;
  outline: none;
  transition: all 0.15s;
}

.form-input:focus, .form-textarea:focus {
  border-color: #6366f1;
  box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.15);
}

.form-tip {
  font-size: 0.75rem;
  color: #94a3b8;
}

.preset-templates {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 1rem;
  flex-wrap: wrap;
}

.preset-label {
  font-size: 0.75rem;
  color: #64748b;
  font-weight: 600;
}

.preset-btn {
  background: #f8fafc;
  border: 1px dashed #cbd5e1;
  padding: 0.2rem 0.6rem;
  border-radius: 4px;
  font-size: 0.75rem;
  color: #475569;
  cursor: pointer;
}

.preset-btn:hover {
  background: #eef2ff;
  color: #4f46e5;
  border-color: #818cf8;
}

.agency-settings-box {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 1rem;
  margin: 1.25rem 0;
}

.box-title {
  font-size: 0.8rem;
  font-weight: 700;
  color: #475569;
  margin-bottom: 0.75rem;
}

.btn-submit {
  width: 100%;
  padding: 0.85rem;
  font-size: 1rem;
  font-weight: 700;
  background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);
  color: #ffffff;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  box-shadow: 0 4px 6px -1px rgba(79, 70, 229, 0.3);
}

.btn-submit:hover:not(:disabled) {
  background: linear-gradient(135deg, #4f46e5 0%, #4338ca 100%);
}

.btn-submit:disabled {
  opacity: 0.65;
  cursor: not-allowed;
}

/* Side Column */
.side-col {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.pitch-card {
  background: linear-gradient(135deg, #fef3c7 0%, #fffbeb 100%);
  border: 1px solid #fde68a;
}

.pitch-title {
  font-size: 1rem;
  font-weight: 700;
  color: #92400e;
  margin-bottom: 0.75rem;
}

.pitch-list {
  padding-left: 1.25rem;
  font-size: 0.85rem;
  color: #78350f;
  line-height: 1.7;
}

.history-card {
  flex: 1;
}

.history-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.history-title {
  font-size: 1rem;
  font-weight: 700;
  color: #1e293b;
}

.btn-refresh {
  background: none;
  border: none;
  font-size: 0.8rem;
  color: #6366f1;
  cursor: pointer;
  font-weight: 600;
}

.history-list {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.history-item {
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 0.75rem;
  background: #f8fafc;
}

.history-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.h-company {
  font-size: 0.85rem;
  font-weight: 700;
  color: #0f172a;
}

.h-score {
  font-size: 0.85rem;
  font-weight: 800;
  padding: 0.15rem 0.45rem;
  border-radius: 4px;
}

.score-danger { background: #fee2e2; color: #b91c1c; }
.score-ok { background: #dcfce7; color: #15803d; }

.history-bottom {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 0.4rem;
  font-size: 0.75rem;
  color: #64748b;
}

.h-link {
  color: #4f46e5;
  text-decoration: none;
  font-weight: 600;
}

.history-empty {
  font-size: 0.85rem;
  color: #94a3b8;
  text-align: center;
  padding: 2rem 0;
}

/* Radar Animation Backdrop */
.radar-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(15, 23, 42, 0.85);
  backdrop-filter: blur(8px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
}

.radar-box {
  text-align: center;
  color: #ffffff;
}

.radar-scanner {
  width: 90px;
  height: 90px;
  border-radius: 50%;
  border: 3px solid rgba(99, 102, 241, 0.3);
  border-top-color: #818cf8;
  animation: spin 1.2s linear infinite;
  margin: 0 auto 1.5rem;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.radar-title {
  font-size: 1.5rem;
  font-weight: 800;
}

.radar-sub {
  font-size: 0.9rem;
  color: #94a3b8;
  margin-top: 0.5rem;
}

.radar-status {
  font-size: 0.8rem;
  color: #6366f1;
  background: #1e1b4b;
  padding: 0.4rem 1rem;
  border-radius: 999px;
  margin-top: 1.25rem;
  display: inline-block;
}
</style>
