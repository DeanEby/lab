public class Student {
    private int studentID;
    private String studentName;
    private String collegeName;
    private String address;
    public Student(int id, String sname, String cname, String addr ) {
        this.studentID = id;
        this.studentName = sname;
        this.collegeName = cname;
        this.address = addr;        
    }
    public int getStudentID(){
        return this.studentID;
    }
    public void setStudentID(int newId){
        this.studentID = newId;
    }
    public String getStudentName(){
        return this.studentName;
    }
    public void setStudentName(String newStudentName){
        this.studentName = newStudentName;
    }
    public String getCollegeName(){
        return this.collegeName;
    }
    public void setCollegeName(String newCollegeName){
        this.collegeName = newCollegeName;
    }
    public String getAddress(){
        return this.address;
    }
    public void setAddress(String newAddress){
        this.address = newAddress;
    }
}


class TestStudent{
    public static void main ( String args[]) {
        Student testStudent = new Student(1234, "Mark", "Harvard", "1234 Easy Street");
        System.out.println(testStudent.getStudentName());
        testStudent.setStudentName("Bob");
        System.out.println(testStudent.getStudentName());
        System.out.println(testStudent.getStudentID());
        testStudent.setStudentID(2468);
        System.out.println(testStudent.getStudentID());
        System.out.println(testStudent.getCollegeName());
        testStudent.setCollegeName("yale");
        System.out.println(testStudent.getCollegeName());
        System.out.println(testStudent.getAddress());
        testStudent.setAddress("the bad place");
        System.out.println(testStudent.getAddress());
    }
}