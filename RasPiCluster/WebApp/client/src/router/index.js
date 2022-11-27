// import Vue from 'vue';
import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView'
import NotFound from '../views/NotFound'
import NotificationView from '../views/NotificationView'



// Vue.use(VueRouter);

const routes = [
    {
        path: '/',
        component: HomeView,
    },
    {
        path: '/notifications',
        component: NotificationView
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