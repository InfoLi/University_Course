// 第六章实验3小狗的状态
// 代码1
public void showState(){
	System.out.println ("狂叫，并冲向去狠咬敌人");
};
// 代码2
public void showState(){
	System.out.println ("晃动尾巴，表示欢迎");
};
// 代码3
public void showState(){
	System.out.println ("嬉戏");
};

// 第七章实验1内部购物卷
InnerPurchaseMoney purchaseMoney1; // 代码1
InnerPurchaseMoney purchaseMoney2; // 代码2
purchaseMoney1=new InnerPurchaseMoney(20000); // 代码3
purchaseMoney2=new InnerPurchaseMoney(10000); // 代码4

// 第8章实验3比较日期
Calendar.getInstance();     // 代码1初始化日历对象
calendar.set(yearOne,monthOne,dayOne);  // 代码2 将calendar的时间设置为yearOne年monthOne月dayOne日
calendar.getTimeInMillis(); //代码3 calendar表示的时间转换成毫秒
new Date (timeOne);     //代码4 用timeOne做参数构造date1
Math.abs(timeOne-timeTwo)/(1000*60*60*24);      //代码5 使用timeTwo, timeOne计算两个日期相隔天数
