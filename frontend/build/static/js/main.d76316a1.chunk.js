(this.webpackJsonpfrontend=this.webpackJsonpfrontend||[]).push([[0],{20:function(e,t,n){},21:function(e,t,n){},42:function(e,t,n){"use strict";n.r(t);var c=n(2),s=n.n(c),o=n(13),a=n.n(o),i=(n(20),n(15)),l=n.p+"static/media/logo.6ce24c58.svg",r=(n(21),n(14)),j=n.n(r),d=n(1);var h=function(){var e=Object(c.useState)({}),t=Object(i.a)(e,2),n=t[0],s=t[1];return Object(c.useEffect)((function(){j.a.get("http://127.0.0.1:8000/flask/hello").then((function(e){console.log("SUCCESS",e),s(e)})).catch((function(e){console.log(e)}))}),[]),Object(d.jsx)("div",{className:"App",children:Object(d.jsxs)("header",{className:"App-header",children:[Object(d.jsx)("img",{src:l,className:"App-logo",alt:"logo"}),Object(d.jsx)("p",{children:"React + Flask Tutorial"}),Object(d.jsx)("div",{children:200===n.status?Object(d.jsx)("h3",{children:n.data.message}):Object(d.jsx)("h3",{children:"LOADING"})})]})})},u=function(e){e&&e instanceof Function&&n.e(3).then(n.bind(null,43)).then((function(t){var n=t.getCLS,c=t.getFID,s=t.getFCP,o=t.getLCP,a=t.getTTFB;n(e),c(e),s(e),o(e),a(e)}))};a.a.render(Object(d.jsx)(s.a.StrictMode,{children:Object(d.jsx)(h,{})}),document.getElementById("root")),u()}},[[42,1,2]]]);
//# sourceMappingURL=main.d76316a1.chunk.js.map