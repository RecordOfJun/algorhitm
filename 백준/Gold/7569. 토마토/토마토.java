import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class ripe{
    int x;
    int y;
    int z;
    public ripe(int z,int y,int x){
        this.x=x;
        this.y=y;
        this.z=z;
    }
}

public class Main {
    static BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int m;
    static int n;
    static int h;
    static int[][][] tomatos;
    static int cnt=0;
    static int convert_cnt=0;
    static int runtime=-1;
    //위,아래,앞,뒤,왼,오
    static int[] dx=new int[] {0,0,1,-1,0,0};
    static int[] dy=new int[] {0,0,0,0,1,-1};
    static int[] dz=new int[] {1,-1,0,0,0,0};
    static Queue<ripe> queue=new LinkedList<>();
    public static void main(String[] args) throws Exception{
        st=new StringTokenizer(br.readLine());
        m=Integer.parseInt(st.nextToken());
        n=Integer.parseInt(st.nextToken());
        h=Integer.parseInt(st.nextToken());

        tomatos=new int[h][n][m];

        initTomatos();
        spreadTomato();

        if(cnt==convert_cnt){
            System.out.println(runtime);
        }
        else {
            System.out.println(-1);
        }
    }

    static void initTomatos() throws  Exception{
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < n; j++) {
                st=new StringTokenizer(br.readLine());
                for (int k = 0; k < m; k++) {
                    int t=Integer.parseInt(st.nextToken());
                    if(t==0){
                        cnt+=1;
                    } else if (t==1) {
                        queue.add(new ripe(i,j,k));
                    }
                    tomatos[i][j][k]=t;
                }
            }
        }
    }

    static void spreadTomato(){
        while (!queue.isEmpty()){
            Queue<ripe> tmpQueue=new LinkedList<>();
            runtime+=1;
            while (!queue.isEmpty()){
                ripe t=queue.poll();
                for (int i = 0; i < 6; i++) {
                    int nx = t.x + dx[i];
                    int ny = t.y + dy[i];
                    int nz = t.z + dz[i];
                    if (nx < 0 || nx >= m || ny < 0 || ny >= n || nz < 0 || nz >= h) {
                        continue;
                    }
                    if (tomatos[nz][ny][nx] == 1 || tomatos[nz][ny][nx] == -1) {
                        continue;
                    }
                    tomatos[nz][ny][nx] = 1;
                    convert_cnt += 1;
                    tmpQueue.add(new ripe(nz, ny, nx));
                }
            }
            queue=tmpQueue;
        }
    }
}
