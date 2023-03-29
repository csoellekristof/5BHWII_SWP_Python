public class App{

    public static void main(String[] args){

        Drucker drucker1 = new ColorDrucker();
        Drucker drucker2 = new SWDrucker();

        String text = "Hallo";

        drucker1.print(text);
        drucker2.print(text);

        drucker1 = switchDrucker(drucker1);
        drucker2 = switchDrucker(drucker2);

        drucker1.print(text);
        drucker2.print(text);

    }


    private static Drucker switchDrucker(Drucker drucker){
        String className = drucker.getClass().getName();
    
        if(className.equals("ColorDrucker")){
            drucker = new SWDrucker();
        

        }
        else if (className.equals("SWDrucker")){
            drucker = new ColorDrucker();
        }
        return drucker;

    }

}