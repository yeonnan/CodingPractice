package exercise.chapter_37;

public class InterfaceTest {
    public static void main(String[] args) {
        //Male 3개 남편, 아빠, 회사원

        HusbandRole male = new Male("철수");
        Wife wife = new Female("영희");

        male.sayLoveEveryDay();
        male.takeCareWife(wife);

        //이어서 아빠
        DaddyRole maleDaddy = (DaddyRole) male; //철수 롤 그대로
        Baby baby = new Baby("임현식");

        maleDaddy.educateBaby(baby);
        maleDaddy.sayLoveEveryDay();

        //회사원. 객체는 제일 상단의 철수 같은 객체이지만 타입만 바꾸고 있는 중
        EmployeeRole maleEmployee = (EmployeeRole) maleDaddy;
        EmployeeRole maleEmployeeTwo = new MaleTwo("민철");

        maleEmployee.workTogether(maleEmployeeTwo);

    }
}
