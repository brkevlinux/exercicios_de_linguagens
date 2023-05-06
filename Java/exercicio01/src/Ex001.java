import java.util.Scanner;
public class Ex001 {

	public static void main(String[] args) {
		// Exercicios ex001, ex002, ex003, ex007 em java.
		Scanner tecla = new Scanner(System.in);
		System.out.println("Olá qual é o seu nome?");
		String nome = tecla.nextLine();
		System.out.format("Seja bem vindo %s \n", nome);
		System.out.print("Digite a sua primeira nota: ");
		float nota1 = tecla.nextFloat();
		System.out.print("Digite a sua segunda nota: ");
		float nota2 = tecla.nextFloat();
		float media = (nota1 + nota2) / 2f;
		System.out.format("A sua média é: %.2f", media);

	}

}
