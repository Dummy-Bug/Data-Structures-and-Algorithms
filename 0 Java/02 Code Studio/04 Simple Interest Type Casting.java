// https://www.codingninjas.com/codestudio/guided-paths/basics-of-java/content/120300/offering/1459166?leftPanelTab=0
import java.util.Scanner;

class Solution {
    
    public static void main(String args[]) {
        
        Scanner sc = new Scanner(System.in);
        
        int principal = sc.nextInt();
        double rate = sc.nextDouble();
        int time = sc.nextInt();
        
        int si = (int)(principal * rate * time) / 100;
        
        System.out.println(si);
        
    }
}