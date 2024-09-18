```
import sympy

# 泊松过程推导的基础：求以下函数的极限
x = sympy.Symbol("x")
f = (1+(1/x))**x
res = sympy.limit(e=f, z=x, z0=sympy.oo)

print("求得的极限数值是", res.evalf())
# 参考：https://wizardforcel.gitbooks.io/scipy-lecture-notes/content/15.html
```
