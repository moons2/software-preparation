# SYSTEM DESIGN

- Um Design de Sistemas de sucesso conta com 3 principios fundamentais
	1.	Pensamento Analitico: a abilidade de quebrar um problema grande
		em pequenos problemas, facil de compreender

Aprendendo sobre Design de Sistemas com o exemplo **Sistema de Serviço de Stream de Música (Spotify, Apple Music, Youtube Music)**.

Um Design de Sistema cobre

## 1. Escopo

Define o que sera tratado e o que não sera tratado. Também oferece um contexto para a audiencia.

## 2. Componentes Chave

Descreve como o audio será armazenado, como será distribuido para diferentes localidades, e como isso é feito com baixa latencia.

## 3. Data Model

Consiste da descrição e categorização dos dados do negócio. A modelagem de dados permite saber quais dados há em seu poder, o significado, descrição, como se relacionam entre si, e de quais fontes provêm.

Modelo Conceitural > Lógico > Físico.

## 4. Escala sob demanda

Definição de assuntos como CDN, Load Balance, tolerancia a falhas, replicação e afins.


---

## 1. ESCOPO

Pertence ao escopo:
-	CreateAccount
-	Uploading music by publisher
-	Distribute the music
-	Search the music
-	Listen to the music
-	Add to PlayList

Não pertence ao escopo
-	Cliente App
-	Unplublishing the audio, video
-	Remove form playlist

Definição de APIs para um MVP

```
accountService(app_key, username, password, address)

uploadService(app_key, albumType, artists, market, labels, name, releaseDate, tracks, restrictions, url)

searchService(app_key, market, albumTitle, trackTitle)

addToPlayListService(app_key, playlistID, trackID)

viewService(app_key, songID)
	service used to play the audio

paymentService(app_key, cardInfo)
```

## 2. COMPONENTES CHAVE

## 3. DATA MODEL

Afim de permitir a utilização de microsserviços, há multiplos schemas.

Quando falamos sobre Design de Sistemas, falamos também sobre o plano de capacidade,
i.e., a estima de armazenamento que o sistema conterá.

para uma relação do tipo USUARIO conforme apresentado na tabela

|   USER   | BYTES |
|:--------:|:-----:|
|  userId  |   6   |
|   name   |   30  |
|   email  |   30  |
|   phone  |   15  |
| username |   30  |
| password |   30  |
|  address |  100  |

total 241 BYTES

Para uma quantia de 200 milhoes de usuarios

(200x10e9) x 241 Bytes = 48,2 Gb

## 4. ESCALA SOB DEMANDA

### 

## 

1. Tech Stack Used

2. Fault Tolerance

3. High Availability

4. Performance

5. Backup

6. Deployment

7. Security

8. Monitoring

9. Logging

10. Scaling the system

11. Storage

12. Maintenance

13. Capital and Operational cost

# DESIGN PARKING GARAGE

```html

<section title="Product Requirements">
	-	necessario poder reservar um ponto de estacionamento
		e receber um recibo
	-	necessario poder pagar pelo pondo de estacionamento
	-	o sistema deve garantir que duas pessoas não reservem
		a mesma vaga ao mesmo tempo
	-	3 tipos de veiculos {compacto, regular, grande}
	-	
</section>

```

# LOAD BALANCER

Load balancer, or a Distributed Queue 

