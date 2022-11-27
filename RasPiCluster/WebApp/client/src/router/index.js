// import Vue from 'vue';
import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView'
import NotFound from '../views/NotFound'
import NotificationView from '../views/NotificationView'
import SensorNodeView from '../views/SensorNodeView'
import StatisticsView from '../views/StatisticsView'
import TeamView from '../views/TeamView'



// Vue.use(VueRouter);

const routes = [
    {
        path: '/',
        component: HomeView,
    },
    {
        path: '/sensor-node',
        component: SensorNodeView
    },
    {
        path: '/notifications',
        component: NotificationView
    },
    {
        path: '/statistics',
        component: StatisticsView
    },
    {
        path: '/team',
        component: TeamView
    },
    // catch all 404
    {
        path: '/:catchAll(.*)',
        component: NotFound
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router;