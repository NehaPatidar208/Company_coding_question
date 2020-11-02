import java.util.*;
class Restclass{
  static int longestDecreasingSubString(String s){
    int res =0,mx=1;
    for(int i=1;i<s.length();i++){
      if (s.charAt(i)<=s.charAt(i-1)){
        mx+=1;
      }else{
        res=max(res,mx);
        mx=1;
      }
    }
    res=max(res,mx);
    return res;
  }
  public static int max(int a,int b){
    if (a>b) return a;
    return b;
  }
}

public class Main{
  public static void main(String [] args){
  Scanner s=new Scanner(System.in);
  int t=s.nextInt();
  Restclass r=new Restclass();
  while (t-->=0){
    String st=s.next();
    System.out.println(r.longestDecreasingSubString(st));
  }
  }
}
