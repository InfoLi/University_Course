import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class windows extends JFrame{
    JFrame window1;
    JPanel panel;
    JTextField userText;
    JPasswordField passwordText;
    JButton loginButton;
    JButton registerButton;
    ActionListener loginlistener;
    ActionListener registerlistener;
    public windows() {
        init();
        window1.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        window1.setVisible(true);
    }
    void init(){
        // 布局
        window1 = new JFrame("代办事项管理系统");
        window1.setBounds(650,150,700,600);

        panel = new JPanel();
        window1.add(panel);
        panel.setLayout(null);

        JLabel title = new JLabel("代办事项管理系统");
        title.setFont(new Font(null, Font.PLAIN, 25));
        title.setBounds(244,50,200,100);
        panel.add(title);

        JLabel userLabel = new JLabel("User:");
        userLabel.setBounds(200,160,80,25);
        panel.add(userLabel);

        userText = new JTextField(20);
        userText.setBounds(300,160,175,25);
        panel.add(userText);

        JLabel passwordLabel = new JLabel("Password:");
        passwordLabel.setBounds(200,190,80,25);
        panel.add(passwordLabel);

        passwordText = new JPasswordField(20);
        passwordText.setBounds(300,190,175,25);
        panel.add(passwordText);

        loginButton = new JButton("login");
        loginButton.setBounds(220, 250, 80, 25);
        panel.add(loginButton);

        registerButton = new JButton("register");
        registerButton.setBounds(370, 250, 80, 25);
        panel.add(registerButton);


        //  监视器
        loginlistener = new loginlisten();
        loginButton.addActionListener(loginlistener);

        registerlistener = new registerlisten();
        registerButton.addActionListener(registerlistener);
    }
    // 监视器功能实现
    public class loginlisten implements ActionListener{
        public void actionPerformed(ActionEvent e) {
            String userstr = userText.getText();
            String passwordrstr = passwordText.getText();
            System.out.println("login");
            SQloperate sql = new SQloperate();
            int flag=sql.accountcheck(userstr,passwordrstr);
            if(flag==1)
            {
                System.out.println("登录成功");
                window1.dispose();
                new home();
            }
            else if (flag==0) {
                System.out.println("登录失败");
                JOptionPane.showMessageDialog(panel, "账号不存在或账户密码错误", "Wrong",JOptionPane.WARNING_MESSAGE);
            }
            else
            {
                System.out.println("wrong");
                JOptionPane.showMessageDialog(panel, "未知错误", "Wrong",JOptionPane.ERROR_MESSAGE);
            }
//            System.out.println(userstr);
//            System.out.println(passwordrstr);
        }
    }
    public class registerlisten implements ActionListener{
        public void actionPerformed(ActionEvent e) {
            String userstr = userText.getText();
            String passwordrstr = passwordText.getText();
            System.out.println("register");
            SQloperate sql = new SQloperate();
            int flag=sql.registercheck(userstr,passwordrstr);
            if (flag ==1){
                System.out.println("注册成功");
                JOptionPane.showMessageDialog(panel, "注册成功", "Message",JOptionPane.INFORMATION_MESSAGE);
            }
            else if (flag == 0){
                System.out.println("注册失败");
                JOptionPane.showMessageDialog(panel, "账号名字已存在", "Wrong",JOptionPane.WARNING_MESSAGE);
            }
            else {
                System.out.println("wrong");
                JOptionPane.showMessageDialog(panel, "未知错误", "Wrong",JOptionPane.ERROR_MESSAGE);
            }
        }
    }
}

