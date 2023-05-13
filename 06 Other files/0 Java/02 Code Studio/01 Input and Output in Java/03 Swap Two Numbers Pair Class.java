// https://www.codingninjas.com/codestudio/guided-paths/basics-of-java/content/120300/offering/1459165?leftPanelTab=1

import javafx.util.Pair;

public class Solution 
{
    public static Pair < Integer, Integer > swap(Pair < Integer, Integer > swapValues) 
    {
        // Write your code here.
        Integer first_val  =  swapValues.getKey();
        Integer second_val =  swapValues.getValue();
        
        Integer temp ;
        temp = first_val;
        first_val = second_val;
        second_val = temp;
  
        return ( new Pair <Integer,Integer>(first_val,second_val) );
    }
}