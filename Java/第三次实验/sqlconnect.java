import java.sql.*;
public class sqlconnect {
    public static void main(String args[]){
        Connection con = null;
        Statement sql;
        ResultSet rs;
        // 加载jdbc-MySQL驱动
        try{
            Class.forName("com.mysql.cj.jdbc.Driver");
        }
        catch (Exception e){}

        String uri = "jdbc:mysql://localhost/student?useSSL=true&characterEncoding=utf-8&serverTimezone=UTC";
        String user = "root";
        String password = "a11129718";
        //连接代码
        try{
            con = DriverManager.getConnection(uri,user,password);
            System.out.println("连接成功");
        }
        catch(SQLException e){
            System.out.println("连接失败");
            System.out.println(e);
        }
        try{
            sql = con.createStatement();
            rs = sql.executeQuery("SELECT * FROM s_user");
            while(rs.next()) {
                int id = rs.getInt(1);
                String name = rs.getString(2);
                System.out.printf("%d\t",id);
                System.out.printf("%s\n",name);
            }
            con.close(); //关闭连接
        }
        catch (SQLException e){
            System.out.println(e);
        }
    }
}
