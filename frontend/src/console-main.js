import { createApp } from 'vue';
import ConsoleApp from './ConsoleApp.vue';
import consoleRouter from './router/console';
import './style.css';

const app = createApp(ConsoleApp);
app.use(consoleRouter);
app.mount('#console-app');
