abstract class Bank2 {
    abstract float getRateOfInterest();
}

class SSS extends Bank2{
    float getRateOfInterest(){
        return .07f;
    }
}

class PNB extends Bank2{
    float getRateOfInterest(){
        return .08f;
    }
}

class TestBank{
    public static void main ( String args[]) {
        Bank2 sbi = new SSS();
        Bank2 pnb = new PNB();
        System.out.println(sbi.getRateOfInterest());
        System.out.println(pnb.getRateOfInterest());
    }
}
