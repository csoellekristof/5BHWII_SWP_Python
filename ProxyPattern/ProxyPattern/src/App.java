public class App{

    public static void main(String[] args){

        Drucker drucker1 = new ColorDrucker();
        Drucker drucker2 = new SWDrucker();

        String text = "Hallo";

        drucker1.print(text);
        drucker2.print(text);

        drucker1 = switchDrucker(drucker1,"SWDrucker");
        drucker2 = switchDrucker(drucker2,"ColorDrucker");

        drucker1.print(text);
        drucker2.print(text);

    }


    private static Drucker switchDrucker(Drucker drucker, String type){
    
        switch(type){
            case "ColorDrucker":
            drucker = new ColorDrucker();
            break;
            case "SWDrucker":
            drucker = new SWDrucker();
            break;
            default:
            System.out.print("False input");
            return drucker;

        }
        return drucker;

    }

}