// bank_example from revature study guide
class Bank{
    float interestRate = 0.01f;

    public float getRateOfInterest(){
        return interestRate;
    }
}

class SBI extends Bank{
    float interestRate = 0.08f;
    public float getRateOfInterest(){
        return interestRate;
    }
}

class ICICI extends Bank{
    ICICI() {
        interestRate = 0.07f;
    }
    public float getRateOfInterest(){
        return 0.07f;
    }
}
class AXIS extends Bank{
    AXIS() {
        interestRate = 0.09f;
    }
    public float getRateOfInterest(){
        return interestRate;
    }
}

class Main {
    public static void main ( String args[]) {
        Bank regbank = new Bank();
        Bank sbi = new SBI();
        ICICI icici = new ICICI();
        AXIS axis = new AXIS();
        System.out.println("bank: " + regbank.getRateOfInterest());
        System.out.println("SBI: " + sbi.getRateOfInterest());
        System.out.println("ICICI: " + icici.getRateOfInterest());
        System.out.println("Axis: " + axis.getRateOfInterest());
        
    
    }
}


