import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;

public class Main{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n, k;
        System.out.println("");
        n = scanner.nextInt();
        k = scanner.nextInt();

        Queue<Integer> queue = new LinkedList<>();

        for(int i = 0 ; i < n; i++){
            queue.offer(i+1);
        }

        //String str = "";
        String[] intArr = new String[n];
        int idx = 0;
        while(queue.size()>0){
            for(int j = 0 ; j < k-1; j++){
                queue.offer(queue.poll());
            }
            //str += Integer.toString(queue.poll())+", "
            intArr[idx++] = Integer.toString(queue.poll());
        }
        String.join(", ", intArr);
        //str = "<"+intArr+">";
        System.out.print("<"+intArr+">");
    }
}

