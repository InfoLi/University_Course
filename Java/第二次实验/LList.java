class LList<T>{
    // node object
    class Link<T>{     
        T data;
        Link next;
        public Link(){  
            data = null;
            next = null;
        }

        public Link(T val){
            data = val;
            next = null;
        }
    }
    
    Link<T> head = new Link<T>(); 
    public LList(){
        head = new Link();
    }
    // add to tail
    public void add(T val){         
        Link<T> tmp = new Link<T>();
        Link<T> cur = new Link<T>();
        cur = new Link(val);
        tmp = head;
        while(tmp.next != null){
            tmp = tmp.next;
        }
        tmp.next = cur;
        cur.next = null;
    }
    // inset to position
    public boolean insertpos(int position,T val){
        if (position<0 || position>getLength()){
            return false;
        }
        else {
            Link<T> cur = new Link<T>();
            cur = head;
            for (int i =0;i<=position-1;i++){
                cur = cur.next;
            }
            Link<T> tmp = new Link<T>();
            tmp = new Link(val);
            tmp.next = cur.next;
            cur.next = tmp;
            return true;
        }
    }
    // delete a node
    public void remove(int position){
        if (position<0 || position>getLength()){
            return;
        }
        else {
            Link<T> cur = new Link<T>();
            cur = head;
            for (int i =0;i<=position-1;i++){
                cur = cur.next;
            }
            Link<T> tmp = new Link<T>();
            tmp = cur.next;
            cur.next = tmp.next;
        }
    }
    // get length
    public int getLength(){
        int len = 0;
        Link<T> tmp = new Link<T>();
        tmp = head.next;
        while(tmp!=null){
            len++;
            tmp = tmp.next;
        }
        return len;
    }
    // print all the data
    public void show(){
        Link<T> tmp = new Link<T>();
        tmp = head;
        System.out.print("data:");
        while(tmp.next != null){
            System.out.print(tmp.next.data);
            System.out.print("\t");
            tmp = tmp.next;
        }
        System.out.print("\n");
    }
    public void search(T val){
        int number = 0;
        Link<T> tmp = new Link<T>();
        tmp = head.next;
         while(tmp!=null){
            if(tmp.data == val) number++;
            tmp = tmp.next;
        }
        System.out.println(val+" is "+number);
    }
}


