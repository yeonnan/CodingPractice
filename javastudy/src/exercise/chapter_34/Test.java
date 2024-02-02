package exercise.chapter_34;

public class Test {
    public static void main(String[] args){

        Customer customer = new Customer("가나다");
        VIPCustomer vipCustomer = new VIPCustomer("라마바");
        Customer customer2 = new Customer("사아자");

        customer.printMyInfo();
        vipCustomer.printMyInfo();
        customer2.printMyInfo();
    }
}
