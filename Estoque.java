import java.util.Scanner;

public class Estoque {
    public static void main(String[] args) throws Exception {
        

        System.out.println("Informações do Produto 1:");

        Produto  produto = new Produto();

        Scanner entrada = new Scanner (System.in);

        produto.codigoSerie = entrada.nextInt();
        produto.codigoProduto = entrada.next();
        produto.nome = entrada.next();
        produto.categoria = entrada.next();
        produto.quantidade = entrada.nextInt();



        produto.mostraInfo();
    }
}
