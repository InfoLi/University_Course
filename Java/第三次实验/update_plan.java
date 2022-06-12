import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
public class update_plan extends JFrame {
    JFrame jf;
    JPanel panel,p;
    JTextField uptitletext,upendtimetext;
    JTextArea upcontentext;
    JButton updateconfirm;
    ActionListener updateconfirmlistener;
    int ID;
    public update_plan(int id){
        init(id);
        jf.setVisible(true);
        jf.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
    }
    void init(int id){
        ID = id;

        jf = new JFrame("代办事项管理系统");
        jf.setBounds(475,50,1000,900);

        panel = new JPanel(null);
        panel.setBackground(Color.gray);

        // String test = "abcdefghijklmnopqrstuvwxyz";

        SQloperate sql = new SQloperate();
        String [] result = sql.get_iddata(id);

        JLabel id_lab = new JLabel("ID:"+id);
        id_lab.setFont(new Font(null, Font.PLAIN, 25));
        id_lab.setBounds(10,10,900,35);
        panel.add(id_lab);

        JLabel title_lab = new JLabel("标题:"+result[2]);
        title_lab.setFont(new Font(null, Font.PLAIN, 25));
        title_lab.setBounds(10,45,900,35);
        panel.add(title_lab);

        JLabel endtime_lab = new JLabel("截止时间:"+result[1]);
        endtime_lab.setFont(new Font(null, Font.PLAIN, 25));
        endtime_lab.setBounds(10,80,900,35);
        panel.add(endtime_lab);

        JLabel content_lab = new JLabel("内容:"+result[0]);
        content_lab.setFont(new Font(null, Font.PLAIN, 25));
        content_lab.setBounds(10,115,900,35);
        panel.add(content_lab);

        p = new JPanel(null);
        p.setBounds(300,300,600,400);
        p.setBorder(BorderFactory.createLineBorder(Color.GRAY, 3));
        p.setBackground(Color.pink);

        JLabel title = new JLabel("更新事项内容");
        title.setBounds(400,10,250,35);
        title.setFont(new Font(null, Font.PLAIN, 25));

        JLabel update_title = new JLabel("title:");
        update_title.setBounds(10,10,250,35);
        update_title.setFont(new Font(null, Font.PLAIN, 25));
        uptitletext = new JTextField(40);
        uptitletext.setBounds(80,20,175,25);

        JLabel update_endtime = new JLabel("endtime(yy-mm-dd):");
        update_endtime.setBounds(10,45,250,35);
        update_endtime.setFont(new Font(null, Font.PLAIN, 25));
        upendtimetext = new JTextField(40);
        upendtimetext.setBounds(250,55,175,25);

        JLabel update_content = new JLabel("content:");
        update_content.setBounds(10,80,100,35);
        update_content.setFont(new Font(null, Font.PLAIN, 25));
        upcontentext = new JTextArea(30,30);
        upcontentext.setBounds(50,130,500,200);

        updateconfirm = new JButton("更新");
        updateconfirm.setBounds(250, 350, 80, 25);


        p.add(title);
        p.add(update_title);
        p.add(update_endtime);
        p.add(update_content);
        p.add(uptitletext);
        p.add(upendtimetext);
        p.add(upcontentext);
        p.add(updateconfirm);

        panel.add(p);
        jf.add(panel);

        updateconfirmlistener = new updateconfirmlisten();
        updateconfirm.addActionListener(updateconfirmlistener);
    }
    public class updateconfirmlisten implements ActionListener{
        public void actionPerformed(ActionEvent e){
            String title = uptitletext.getText();
            String endtime = upendtimetext.getText();
            String content = upcontentext.getText();
            SQloperate sql = new SQloperate();
            int flag = sql.update_iddata(title,endtime,content,ID);
            if (flag == 1){
                JOptionPane.showMessageDialog(panel, "更新成功", "Message",JOptionPane.INFORMATION_MESSAGE);
            }
            else if (flag == -1){
                JOptionPane.showMessageDialog(panel, "更新失败", "Wrong",JOptionPane.ERROR_MESSAGE);
            }
            jf.dispose();
            new home();
        }
    }
}
