import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;


class Index{
    public int x;
    public int y;
    public Index(int x,int y){
        this.x=x;
        this.y=y;
    }
}

public class Main {
    static int n;
    static int [][] boomMap;
    static char [][] selectedMap;

    static int [] dx=new int[] {-1,-1,0,1,1,1,0,-1};
    static int [] dy=new int[] {0,1,1,1,0,-1,-1,-1};

    static boolean isSelectBoom=false;
    static ArrayList<Index> boomIndexes=new ArrayList<Index>();
    static BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    public static void main(String[] args) throws Exception {
        st=new StringTokenizer(br.readLine());
        n=Integer.parseInt(st.nextToken());
        boomMap=new int[n][n];
        selectedMap=new char[n][n];
        initMap();

        for (int i=0;i<n;i++){
            String input= br.readLine();
            for(int j=0;j<n;j++){
                char c=input.charAt(j);
                if(c=='*'){
                    detectBoom(i,j);
                }
            }
        }

        for(int i=0;i<n;i++){
            String input=br.readLine();
            for(int j=0;j<n;j++){
                char c=input.charAt(j);
                if(c=='x'){
                    select(i,j);
                }
            }
        }

        if(isSelectBoom){
            for (Index boomIndex : boomIndexes) {
                selectedMap[boomIndex.x][boomIndex.y]='*';
            }
        }

        showResult();
    }

    static void initMap(){
        for (int i=0;i<n;i++){
            for (int j=0;j<n;j++){
                boomMap[i][j]=0;
            }
        }

        for (int i=0;i<n;i++){
            for (int j=0;j<n;j++){
                selectedMap[i][j]='.';
            }
        }
    }

    static void detectBoom(int x,int y){
        boomMap[x][y]=-1;
        boomIndexes.add(new Index(x,y));
        for(int i=0;i<8;i++){
            int nx=x+dx[i];
            int ny=y+dy[i];
            if(nx<0 || nx>=n || ny<0|| ny>=n){
                continue;
            }
            if(boomMap[nx][ny]==-1){
                continue;
            }
            boomMap[nx][ny]+=1;
        }
    }

    static void select(int x,int y){
        if(boomMap[x][y]==-1){
            isSelectBoom=true;
        }
        else {
            selectedMap[x][y] = Character.forDigit(boomMap[x][y], 10);
        }
    }

    static void showResult(){
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(selectedMap[i][j]);
            }
            System.out.println();
        }
    }
}
