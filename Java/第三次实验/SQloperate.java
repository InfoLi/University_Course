import java.sql.*;

public class SQloperate {
    Connection con = null;
    Statement sql;
    ResultSet rs;
    void init(){
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

    }
    // 注册账户时数据库检测
    public int accountcheck(String accstr,String passtr){
        init();
        try{
            sql = con.createStatement();
            rs = sql.executeQuery("select account from s_user where account ='"+accstr+"' and password ='"+passtr+"'");
            if (rs.next())
                return (1);
            else
                return (0);
        }
        catch (SQLException e){
            System.out.println(e);
        }
        return (-1);
    }
    // 登录账户时数据库检测
    public int registercheck(String accstr,String passtr){
        init();
        try{
            sql = con.createStatement();
            rs = sql.executeQuery("select account from s_user where account ='"+accstr+"'");
            if (rs.next())
                return (0);
            else{
                String indate = "('"+accstr+"','"+passtr+"')";
                String sqlStr = "insert into s_user values"+indate;
                int ok = sql.executeUpdate(sqlStr);
                return (1);
            }

        }
        catch (SQLException e){
            System.out.println(e);
        }
        return (-1);
    };
    // 数据库数据遍历
    public String[][] getplandata(){
        init();
        try{
            sql = con.createStatement();
            rs = sql.executeQuery("select * from s_todo");
            String [][] str = new String[10000][3];
            int i = 0;
            while(rs.next()){
                String endtime = rs.getString(2);
                String title = rs.getString(3);
                String id = rs.getString(4);
                str[i][0]=endtime;
                str[i][1]=title;
                str[i][2]=id;
                i++;
            }
            return (str);
        }
        catch (SQLException e){
            System.out.println(e);
        }
        return new String[0][0];
    }
    // todo数据表内容添加
    public int addplan(String titlestr,String endtimestr,String contentstr){
        init();
        try{
            int id=0;
            sql = con.createStatement();
            rs = sql.executeQuery("select * from s_todo");
            while(rs.next()){
                id = rs.getInt(4);
            }
            id = id+1;
            String indate = "('"+contentstr+"','"+endtimestr+"','"+titlestr+"',"+id+")";
            String sqlStr = "insert into s_todo values"+indate;
//            System.out.println(sqlStr);
            int ok = sql.executeUpdate(sqlStr);
            return (1);
        }
        catch (SQLException e){
            System.out.println(e);
        }
        return (-1);
    }
    // 查看某项事项的详细内容
    public String querycontent(int id){
        init();
        try{
            sql = con.createStatement();
            rs = sql.executeQuery("select content from s_todo where id ='"+id+"'");
            while(rs.next()){
                String content = rs.getString(1);
                return (content);
            }
        }
        catch (SQLException e){
            System.out.println(e);
        }
        return (new String());
    }
    // 删除某项代办事项
    public int deleteplan(int id){
        init();
        try{
            sql = con.createStatement();
            String sqlStr = "delete from s_todo where id ="+id;
            int ok = sql.executeUpdate(sqlStr);
            return (1);
        }
        catch (SQLException e){
            System.out.println(e);
        }
        return (-1);
    }
    // 获得特定id的代办事项
    public String[] get_iddata(int selct_id){
        init();
        try{
            sql = con.createStatement();
            rs = sql.executeQuery("select * from s_todo where id ="+selct_id);
            String [] str = new String[4];
            while (rs.next()){
                String content = rs.getString(1);
                String endtime = rs.getString(2);
                String title = rs.getString(3);
                String id = rs.getString(4);
                str[0] = content;
                str[1] = endtime;
                str[2] = title;
                str[3] = id;
                return (str);
            }
        }
        catch (SQLException e){
            System.out.println(e);
        }
        return new String[0];
    }
    // 更新特定id的代办事项
    public int update_iddata(String title,String endtime,String content,int id){
        init();
        try{
            sql = con.createStatement();
            String sqlStr = "update s_todo set content ='"+content+"',endtime ='"+endtime+"',title ='"+title+"' where id= '"+id+"'";
            int ok = sql.executeUpdate(sqlStr);
            return (1);
        }
        catch(SQLException e){
            System.out.println(e);
        }
        return (-1);
    }
}
