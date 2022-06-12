import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Vector;

public class home extends JFrame{
    JFrame jf;
    JPanel panel,top,leftmenu,p1,p2,p3,p4,p5;
    JButton plan,add,query,delete,update,planupdate;
    JButton addconfirm,queryconfirm,deleteconfirm,updateconfirm;
    JTextField titletext,endtimetext,queryid_text,deleteid_text,updateid_text;
    JTextArea contentext;
    ActionListener planlistener,addlistener,querylistener,deletelistener,updatelistener,planupdatelistener;
    ActionListener addconfirmlistener,queryconfirmlistener,deleteconfirmlistener,updateconfirmlistener;
    JTable table;
    public home(){
        init();
        jf.setVisible(true);
        jf.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
    }
    void init(){
        jf = new JFrame("代办事项管理系统");
        jf.setBounds(475,50,1000,900);

        panel = new JPanel(null);

        // 表头
        top = new JPanel(null);
        top.setBounds(0,0,1000,100);
        // top.setBackground(Color.blue);

        JLabel userLabel = new JLabel("代办事项管理系统");
        userLabel.setFont(new Font("Dialog", Font.PLAIN, 35));
        userLabel.setBounds(375,0,1000,100);
        top.add(userLabel);

        // 左侧菜单栏
        leftmenu = new JPanel(null);
        leftmenu.setBounds(0,100,150,800);
        // leftmenu.setBackground(Color.GREEN);

        plan = new JButton("已规划日程");
        plan.setBounds(0,0,150,100);
        leftmenu.add(plan);

        add = new JButton("添加代办事项");
        add.setBounds(0,100,150,100);
        leftmenu.add(add);

        query = new JButton("查看某项代办事项");
        query.setBounds(0,200,150,100);
        leftmenu.add(query);

        delete = new JButton("删除某项代办事项");
        delete.setBounds(0,300,150,100);
        leftmenu.add(delete);

        update = new JButton("更新某项代办事项");
        update.setBounds(0,400,150,100);
        leftmenu.add(update);

        planupdate = new JButton("更新已规划日程");
        planupdate.setBounds(0,500,150,100);
        leftmenu.add(planupdate);

        // p1 已规划日程
        p1 = new JPanel(null);
        p1.setBounds(150,100,850,800);
//        p1.setBackground(Color.magenta);
        setdatashow();

        // p2 添加代办事项
        p2 = new JPanel(null);
        p2.setBounds(250,200,600,400);
        p2.setBorder(BorderFactory.createLineBorder(Color.GRAY, 3));
        p2.setBackground(Color.pink);
        setp2();

        // p3 查看某项代办事项
        p3 = new JPanel(null);
        p3.setBounds(250,200,600,400);
        p3.setBorder(BorderFactory.createLineBorder(Color.GRAY, 3));
        p3.setBackground(Color.pink);
        setp3();

        // p4 删除某项代办事项
        p4 = new JPanel(null);
        p4.setBounds(250,200,600,400);
        p4.setBorder(BorderFactory.createLineBorder(Color.GRAY, 3));
        p4.setBackground(Color.pink);
        setp4();

        // p5 更新某项代办事项
        p5 = new JPanel(null);
        p5.setBounds(250,200,600,400);
        p5.setBorder(BorderFactory.createLineBorder(Color.GRAY, 3));
        p5.setBackground(Color.pink);
        setp5();


        // 布局添加
        jf.add(panel);
        panel.add(top);
        panel.add(leftmenu);
        panel.add(p1);
        panel.add(p2);
        panel.add(p3);
        panel.add(p4);
        panel.add(p5);
        p1.setVisible(true);
        p2.setVisible(false);
        p3.setVisible(false);
        p4.setVisible(false);
        p5.setVisible(false);

        //  监视器 plan,add,query,delete,update,planupdate
        planlistener = new planlisten();
        plan.addActionListener(planlistener);
        addlistener = new addlisten();
        add.addActionListener(addlistener);
        querylistener = new querylisten();
        query.addActionListener(querylistener);
        deletelistener = new deletelisten();
        delete.addActionListener(deletelistener);
        updatelistener = new updatelisten();
        update.addActionListener(updatelistener);
        planupdatelistener = new planupdatelisten();
        planupdate.addActionListener(planupdatelistener);

        // 监视器 addconfirm,queryconfirm,deleteconfirm,updateconfirm;
        addconfirmlistener = new addconfirmlisten();
        addconfirm.addActionListener(addconfirmlistener);

        queryconfirmlistener = new queryconfirmlisten();
        queryconfirm.addActionListener(queryconfirmlistener);

        deleteconfirmlistener = new deleteconfirmlisten();
        deleteconfirm.addActionListener(deleteconfirmlistener);

        updateconfirmlistener = new updateconfirmlisten();
        updateconfirm.addActionListener(updateconfirmlistener);
    }
    // 已规划日程的表格显示
    public void setdatashow(){
        SQloperate sql = new SQloperate();
        String[][] data = sql.getplandata();    // emdtime,title,id

        table=new JTable();
        DefaultTableModel tableModel = (DefaultTableModel) table.getModel();

        tableModel.addColumn("id");
        tableModel.addColumn("截止时间");
        tableModel.addColumn("代办事项标题");
        for (int i = 0; i < data.length; i++) {
            String[] o={data[i][2],data[i][0],data[i][1]};
            tableModel.addRow(o);
        }

        table.getTableHeader().setResizingAllowed(false);               // 设置表头不允许手动改变列宽
        table.getTableHeader().setReorderingAllowed(false);             // 设置表头不允许拖动重新排序各列
        table.setRowHeight(30);                                         // 设置行高
        table.setFont(new Font(null, Font.PLAIN, 14));       // 设置字体大小
        table.setBounds(100,50,550,200);
        table.setSelectionForeground(Color.DARK_GRAY);      // 选中后字体颜色
        table.setSelectionBackground(Color.cyan);           // 选中后字体背景

        JScrollPane scrollPane = new JScrollPane(table);     // 把表格放到滚动面板中（表头将自动添加到滚动面板顶部）
        scrollPane.setBounds(0,0,835,750);
        p1.add(scrollPane);     // 添加 滚动面板 到 内容面板
        scrollPane.setVerticalScrollBarPolicy(ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS);

    }
    public void updatedata(){
        jf.dispose();
        new home();
    }
    public void setp2(){
        JLabel title = new JLabel("添加代办内容");
        title.setBounds(400,10,250,35);
        title.setFont(new Font(null, Font.PLAIN, 25));

        JLabel add_title = new JLabel("title:");
        add_title.setBounds(10,10,250,35);
        add_title.setFont(new Font(null, Font.PLAIN, 25));
        titletext = new JTextField(40);
        titletext.setBounds(80,20,175,25);

        JLabel add_endtime = new JLabel("endtime(yy-mm-dd):");
        add_endtime.setBounds(10,45,250,35);
        add_endtime.setFont(new Font(null, Font.PLAIN, 25));
        endtimetext = new JTextField(40);
        endtimetext.setBounds(250,55,175,25);

        JLabel add_content = new JLabel("content:");
        add_content.setBounds(10,80,100,35);
        add_content.setFont(new Font(null, Font.PLAIN, 25));
        contentext = new JTextArea(30,30);
        contentext.setBounds(50,130,500,200);
//        contentext.setBackground(Color.pink);

        addconfirm = new JButton("添加");
        addconfirm.setBounds(250, 350, 80, 25);

        p2.add(title);
        p2.add(add_title);
        p2.add(add_endtime);
        p2.add(add_content);
        p2.add(titletext);
        p2.add(endtimetext);
        p2.add(contentext);
        p2.add(addconfirm);
    }
    public void setp3(){
        JLabel query_title = new JLabel("查询事项");
        query_title.setBounds(200,10,250,35);
        query_title.setFont(new Font(null, Font.PLAIN, 35));

        JLabel query_id = new JLabel("id:");
        query_id.setBounds(90,110,250,35);
        query_id.setFont(new Font(null, Font.PLAIN, 25));
        queryid_text = new JTextField(15);
        queryid_text.setBounds(160,117,175,25);

        queryconfirm = new JButton("查询");
        queryconfirm.setBounds(350,117,80,25);

        p3.add(query_title);
        p3.add(query_id);
        p3.add(queryid_text);
        p3.add(queryconfirm);
    }
    public void setp4(){
        JLabel delete_title = new JLabel("删除事项");
        delete_title.setBounds(200,10,250,35);
        delete_title.setFont(new Font(null, Font.PLAIN, 35));

        JLabel query_id = new JLabel("id:");
        query_id.setBounds(90,110,250,35);
        query_id.setFont(new Font(null, Font.PLAIN, 25));
        deleteid_text = new JTextField(15);
        deleteid_text.setBounds(160,117,175,25);

        deleteconfirm = new JButton("删除");
        deleteconfirm.setBounds(350,117,80,25);

        p4.add(delete_title);
        p4.add(query_id);
        p4.add(deleteid_text);
        p4.add(deleteconfirm);
    }
    public void setp5(){
        JLabel title = new JLabel("更新事项");
        title.setBounds(200,10,250,35);
        title.setFont(new Font(null, Font.PLAIN, 35));


        JLabel id = new JLabel("id:");
        id.setBounds(90,110,250,35);
        id.setFont(new Font(null, Font.PLAIN, 25));
        updateid_text = new JTextField(15);
        updateid_text.setBounds(160,117,175,25);

        updateconfirm = new JButton("查找更新");
        updateconfirm.setBounds(350,117,150,25);

        p5.add(title);
        p5.add(id);
        p5.add(updateid_text);
        p5.add(updateconfirm);
    }

    // 监视器功能实现
    // 菜单栏按钮
    // planlisten,addlisten,querylisten,deletelisten,updatelisten,planupdatelisten
    public class planlisten implements ActionListener{
        public void actionPerformed(ActionEvent e){
            p1.setVisible(true);
            p2.setVisible(false);
            p3.setVisible(false);
            p4.setVisible(false);
            p5.setVisible(false);
        }
    }
    public class addlisten implements ActionListener{
        public void actionPerformed(ActionEvent e){
            p1.setVisible(false);
            p2.setVisible(true);
            p3.setVisible(false);
            p4.setVisible(false);
            p5.setVisible(false);
        }
    }
    public class querylisten implements ActionListener{
        public void actionPerformed(ActionEvent e){
            p1.setVisible(false);
            p2.setVisible(false);
            p3.setVisible(true);
            p4.setVisible(false);
            p5.setVisible(false);
        }
    }
    public class deletelisten implements ActionListener{
        public void actionPerformed(ActionEvent e){
            p1.setVisible(false);
            p2.setVisible(false);
            p3.setVisible(false);
            p4.setVisible(true);
            p5.setVisible(false);
        }
    }
    public class updatelisten implements ActionListener{
        public void actionPerformed(ActionEvent e){
            p1.setVisible(false);
            p2.setVisible(false);
            p3.setVisible(false);
            p4.setVisible(false);
            p5.setVisible(true);
        }
    }
    public class planupdatelisten implements ActionListener{
        public void actionPerformed(ActionEvent e){
            updatedata();
        }
    }
    // 按钮
    //  addconfirmlisten,queryconfirmlisten,deleteconfirmlisten,updateconfirmlisten;
    public class addconfirmlisten implements ActionListener{
        public void actionPerformed(ActionEvent e){
            String titlestr = titletext.getText();
            String endtimestr = endtimetext.getText();
            String contentstr = contentext.getText();
            SQloperate sql = new SQloperate();
            int flag = sql.addplan(titlestr,endtimestr,contentstr);
            if (flag == 1){
                JOptionPane.showMessageDialog(panel, "添加成功", "Message",JOptionPane.INFORMATION_MESSAGE);
            }
            else if (flag == -1){
                JOptionPane.showMessageDialog(panel, "添加失败", "Wrong",JOptionPane.ERROR_MESSAGE);
            }
        }
    }
    public class queryconfirmlisten implements ActionListener{
        public void actionPerformed(ActionEvent e){
            String id_str = queryid_text.getText();
            int id = Integer.parseInt(id_str);
            SQloperate sql = new SQloperate();
            String content = sql.querycontent(id);
//            System.out.println(content);
            JOptionPane.showMessageDialog(panel, content, "代办事项内容",JOptionPane.INFORMATION_MESSAGE);
        }
    }
    public class deleteconfirmlisten implements ActionListener{
        public void actionPerformed(ActionEvent e){
            String id_str = deleteid_text.getText();
            int id = Integer.parseInt(id_str);
            SQloperate sql = new SQloperate();
            int flag  = sql.deleteplan(id);
            if (flag == 1){
                JOptionPane.showMessageDialog(panel, "删除成功", "Message",JOptionPane.INFORMATION_MESSAGE);
            }
            else if (flag == -1){
                JOptionPane.showMessageDialog(panel, "删除失败", "Wrong",JOptionPane.ERROR_MESSAGE);
            }
        }
    }
    public class updateconfirmlisten implements ActionListener{
        public void actionPerformed(ActionEvent e){
            String id_str = null;
            id_str = updateid_text.getText();
            if (id_str != null & id_str.length()!=0){
                int id = Integer.parseInt(id_str);
                if (id >= 0){
                    new update_plan(id);
                    jf.dispose();
                }
                else{
                    JOptionPane.showMessageDialog(panel, "请输入正确的id", "Wrong",JOptionPane.WARNING_MESSAGE);
                }
            }
            else{
                JOptionPane.showMessageDialog(panel, "请输入正确的id", "Wrong",JOptionPane.WARNING_MESSAGE);
            }
        }
    }
}
