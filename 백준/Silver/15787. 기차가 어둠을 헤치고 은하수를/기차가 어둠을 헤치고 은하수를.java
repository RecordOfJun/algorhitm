import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static int m;
    static BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int[][] train;
    static Set<String> set=new HashSet<String>();
    public static void main(String[] args) throws Exception {
        st=new StringTokenizer(br.readLine());
        n=Integer.parseInt(st.nextToken());
        m=Integer.parseInt(st.nextToken());
        train=new int[n][20];
        initTrain();

        for (int i = 0; i < m; i++) {
            st=new StringTokenizer(br.readLine());
            int command=Integer.parseInt(st.nextToken());
            switch (command){
                case 1:
                    first(Integer.parseInt(st.nextToken())-1,Integer.parseInt(st.nextToken())-1);
                    break;
                case 2:
                    second(Integer.parseInt(st.nextToken())-1,Integer.parseInt(st.nextToken())-1);
                    break;
                case 3:
                    third(Integer.parseInt(st.nextToken())-1);
                    break;
                case 4:
                    fourth(Integer.parseInt(st.nextToken())-1);
                    break;
            }
        }

        for (int i = 0; i < n; i++) {
            set.add(getTrain(i));
        }

        System.out.println(set.size());
    }

    static void initTrain(){
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < 20; j++) {
                train[i][j]=0;
            }

        }
    }

    static void first(int i,int x){
        if(train[i][x]==0){
            train[i][x]=1;
        }
    }

    static void second(int i,int x){
        if(train[i][x]==1){
            train[i][x]=0;
        }
    }

    static void third(int i){
        for (int j = 19; j >= 1; j--) {
            train[i][j]=train[i][j-1];
        }
        train[i][0]=0;
    }

    static void fourth(int i){
        for (int j = 0; j < 19; j++) {
            train[i][j]=train[i][j+1];
        }
        train[i][19]=0;
    }

    static String getTrain(int i){
        StringBuilder sb=new StringBuilder("");
        for (int j = 0; j < 20; j++) {
            sb.append(train[i][j]);
        }
        return sb.toString();
    }
}
