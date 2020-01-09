import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Admin from "../views/Admin.vue";
import Employer from "../views/Employer";
import Employee from "../views/Employee";
import Faq from "../views/FAQ";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: Home
  },
  {
    path: "/admin",
    name: "admin",
    component: Admin,
    props: true
  },
  {
    path: "/employer",
    name: "employer",
    component: Employer,
    props: true
  },
  {
    path: "/employee",
    name: "employee",
    component: Employee,
    props: true
  },
  {
    path: "/faq",
    name: "faq",
    component: Faq
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
