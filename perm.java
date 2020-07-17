import java.util.*;
class perm{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        String st="";
        int count=1;
        char c[] = str.toCharArray();
        int n=c.length;
        for(int i=0;i<n-1;i++){
            if(c[i]==c[i+1]){
                count++;
            }
            if(c[i]!=c[i+1]){
                st = st + c[i]  + String.valueOf(count);
                count = 1;
            }
        }

        st = st + c[n-1] + count;
        //int m=st.length();
        
    

        if(st.length()<str.length()){
            System.out.println(st);
        }
        else{
            System.out.println(str);
        }

    }
}