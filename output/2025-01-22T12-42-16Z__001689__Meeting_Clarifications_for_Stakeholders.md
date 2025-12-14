# Meeting Clarifications for Stakeholders

## You (2025-01-22T12:42:16.437068+00:00)

this is one of the internal meetings we just had among the designers and engineers, who are trying to figure out the next step with the stakeholders and their engineers. Could u read through it in detail and figure out all the questions the attendees of this meeting want to clarify with the stakeholders


_______


You want to know the libraries.
We need to know what, yeah, library you're using, or if they are, if they have any specific preferences for the not required.
Okay, that is question one for John Sakshat, next question. Rishi,
next question, I think I've already seen the bunch of APIs which they have, so I think they are using v5 as of now that was listed in the meeting. So for dashboard, specifically, if they can send like, which API they are using that we need to know, okay, because there are very specific, yeah, because our preference is that good for so only APIs which are used for DAPP code as of now, we need a list of that,
okay? And then you're saying we definitely need that, because the front end code will be developed using the API. Is
that, yeah, integration, but the Data Institute, the data integration will be from from that point of view,
okay, the third question is, AI summaries. Sakshat, have you shown AI summaries? Yeah,
I'll show it once again. I.
Okay, so they have these AI summaries right now. It's, it's only for a select few widgets.
How that might reflect on other widgets. That's unclear as of now. But the idea is, as soon as someone creates a widget like largest concept movement.
It's taking longer to load,
but yeah, the idea is, as soon as you introduce a widget, it will create four or five summaries, each summary referring to a particular concept, so, like Trader Joe's will get its own
summary.
And I think this way they're they're trying to basically find
ways to
introduce different types of summaries.
Oh, I'm sorry, these are the documents. So
the documents are basically each comment. So every user comment, every user feedback, is referred to as one document. So here they're showing out of 94 documents. They're just showing all the documents,
and I think something is supposed to happen if I click on one
embarrassing documents For i
Yeah, so overall, The AI summary As I
to
a dots or esrx, global filters, and everybody could talk to
say, impact of the chart scope
or text summary. I think Sakshat should give you a walkthrough of how to use this thing. He has made a really good
report, sorry.
I think over to you, yeah, sorry. I think Sakshat. There is a gap in Rishis understanding. He was thinking, you colorful charts, me the character,
daylight appetite, he's thinking he wore design, work order, no, no, no, actually, so clear looking code, yeah, so the way we labeling this is, this is the dashboard side. This particular image that you see, and the rest of the app is more of an analytics section.
The way I was thinking I was talking about this one, yeah, so the way a person might open a dashboard is by clicking on the last item here.
Okay, and once that happens,
there's a bunch of things they can do.
So they've segmented different visualizations in this manner
for project. These are,
I don't know how to describe it, but it's basically like metadata. So how many documents? What's the average score?
Any any basic stuff like NPS score, that's sort of globally applicable. Those things come under Project,
and they also have this thing called Text widget where a user can add their own text boxes. Okay,
yeah, so it's, it's like a very traditional text.
X entry, text area, text editor, yeah, so that, and apart from that, they have visualizations. So let's say if I pick something like volume,
most of these are simple, like bar graphs or line charts or things like that. This this small room for editing, like I can probably turn these smooth lines into those Angular, sharp lines, like the ones we see here, so you can have that level of fine customization. There's also filters, so you can filter based on certain concepts. So concept is for them. It's basically like those fields,
key terms. So the key terms, like Costco, shopping, store items, anything that was referenced in all the comment, all the data that they have.
And so this, this is the part we'll be designing for now. But even while designing, we'll have to make sure that whatever we design can be scaled into the rest of the application. So so that's why, earlier, we were talking about making sure that whatever library we pick has enough visualizations, both for this dashboard
and these
sort of Galaxy charts.
I think one requirement is we definitely need their code list.
Sakshat, better to, I think, set up a meeting with John for 30 minutes. Rishi and John and you and me,
okay? Because if we are just writing over email, we need this. We need that. Let's just get on to a call. Maybe John can answer a lot of things immediately, but let's still list on all the questions, yes, yes. So before the meeting, I'll create all the set of questions, and then we can send it before the meeting itself, right? See, this is a very tight deadline project,
so we should show that we are very agile and we can take decisions and move very fast.
So Rishi, if you have opened the same page on your side, View Source, okay, can we figure out what chart libraries they are using? I can, I can drive. I can drive, great,
and try that. And also, I think Sakshat You should help Rishi build one
dashboard and then see, then Rishi should see all the challenges, like text highlights and fly outs coming. Then filters impacting local filters impacting the chart, global filters impacting the chart.
Because if Rishi is asking for APIs, that means we are not just giving
just the chart code, we are giving the whole damn functional piece to them, so they'll just put it in their code.
Right? Yeah,
that's our idea, and we'll be building some templates also for them.
Sakshat, I was also thinking, should we I don't know if that is possible in court, when we land here for the very first time, it's like huge canvas with no directions how to use it. So some kind of onboarding flow will help.
Yeah, it will help, but
we should add it. Actually, I'm not saying no, but I think within the time limit that we have might be
just a little challenging,
because now,
based on how Mark Mark Mandel, not Mark lights, but Mark Mendel,
if we really, really have to help him,
so we need to take some control of how the whole experience, onboarding flow, this help
this template, or meaning thinking the whole experience.
Yeah,
so acting as true consultants, rather than saying, Okay, we'll just do this because you're asking this, that will definitely turn it around, and
they, they'll be able to, I don't know when customers or not, but
at least better, though, yeah, actually, there's even if we, I.
Um, if we don't try to add any ideas as we start building it, as we start making a sort of system, we'll almost
inevitably have to add a whole bunch of things. For example, if we talk about something like summaries, right? So if we simply introduce the idea of customizing a summary, then there's a whole series of components, flows, interactions that we'll have to add without without them even asking for it so and that's one example.
If we go into things like filters,
the sort of fluid interactions that we were talking about yesterday, where users can incorporate KPIs along with
KPIs and text along with the visualizations. Yeah, there's, there's a whole series of
both interactions, components, things we'll have to add
in every piece. So
even one week for me is, like a very tight deadline. Ideally, two and a half weeks would have been nice,
but yeah, within a week we'll have to we're already adding, like, a whole bunch of things.
Okay, so
lick Loic bar onboarding.
Mother made the Markman. Getting lot of things in my mind, but
I just, I still want to keep the conversation structured and objective. I Yeah,
yeah.
She all agree. Take is good job, Minister, AI summary here,
message generator, see and also will be challenge over this code me,
so
it's my key, a key bar chart, banaling. It will make in front end code and all, and then that same will be replicated for others. Or what do you How are you thinking?
What I understood is they have their common
some common library used
to Bucha.
I'm
audible now,
yeah,
they are somehow dragging and dropping the frames. And as soon as you drag and drop the frames,
they start with a real time,
and somehow this gets recorded in their local dash, and whenever you are using the top filter on top,
so doing any change in that filter will basically hit all the APS at one go. Thank you. Sorry. Screen.
So this may take problem here that is related to scaling. Is aware management, coffee, sorry, charge and then I apply filter. So there will be too many APIs, which will be called, which may load rather but that is, I think, performance related issue. That will be their problem. But so far, I was able to understand the individual elements on the left hand side, all of them are having individual kind of screens, income, drag and drop, common interface, and as soon as you drag and drop that sorry API is
for that screen at one Time.
So good concept, actually.
And yes, sorry. Screens is Joe main job from name dollars, you have a frame, and then you basically put elements. Same is here for a party that is a frame and individual elements, and it is having your own properties and all that stuff.
So who saree pieces, a particular is no multiple
pages
or concept yet internal properties me or global civil driven, global level,
other than that, global dependency for pushing here, but to internal dependent surface page, the key so is my
individual.
Any screens in Sakha may come to know whatever it is not like you.
Bucha, it is more like a section individually,
these all are acting as separate pages from front end point
of view. Oh, I didn't think of that because, from my perspective, the way I saw it was
like we have these two widgets here, volume over time and sentiment over time. So from a design point of view, these aren't two separate widgets. It's the same widget. It's just, we'll just have to set some kind of global guidelines for how all these visualizations will render, how the you know, anatomy of the widget will work. But you're saying each of these is like an individual page. So essentially we have, yeah, it is.
It could be possible. What I saw is like, I can see this volume of one time sentiment over one time. It could be possible that these are similar. But what I see, from my point of view, these are all these. Both are separate pages and separate code. Only few elements could be, you know, sort of mismatching in terms of maybe data value, but it's no or we just say other screens, there are other screens which will be completely which would be completely different. I say it takes all apart and all that stuff. Yeah? So those are having their individual goals. Yeah. There are a bunch of widgets that are acting almost in a unique manner, like chemo, like this change concept, yeah.
So it's a separate in this particular chart. Again, it's quite separate. This is completely what we what we can do initially is even if we see that there is a similarity in the screens, right? So we can still, I can still figure out how we are making one code or one, you know, common function, which basically acts for them. But I need to, from, from my end, I need to one, you know, do one this thing research, where I need to list out, what are the similar screens, what are the different ones? So then we can have, like, what combinations we have in terms of, you know, very non similar screens, that will be the value three screens. But Rishi, I'll, I'll try to stay in touch with you. But you know, as part of the whole point of making these experiences fluid,
we may have to also think of some way to customize a widget so that text can be incorporated within that widget as it is. No problems, no problem. I'm just okay, telling me, telling you, from my understanding, you know what they have they might have done. So while designing, you might need to consider these separate screens under whatever you are doing. The customizations part of you see, we are CX team, we need to add something problem with that. But what screens
we need to we need to understand these are separate. Take it as a separate page, like individual screen, which are not the similar screens.
So easily. Rajiv, we need to
take an understanding from them. Key
periva, this is what we understand if they feel, if they feel, Allah here, so they can tell us one part. The second part is definitely to understand this whole thing and give them a clear idea about how much effort we will be needing in terms of timeline. We need their code base because manager, resume, inspector can be searched. But again, code base, medical or I'll be able to understand what are the matching screens? What are the completely different screens? So what a design and development effort,
okay,
meeting to set up career. John Kelly, A, B, okay,
Eastern, 11 year, 10, 3011,
Sakshat,
okay, got it
30 minutes is or like 45 minutes or something.
I think 3031
will be fine, because I
think enough is better Exactly, exactly before the meeting, I'll try to drop all the thing and maybe taking,
okay, I'll also take a transcript of this, and I'll figure out all the questions Rishi that you raised in this discussion. So we'll just show those questions as it is find
the time. So
okay, I've shared a comment, Doc, you can put all that thing over there so I'll just see like I'm not repeating the same question again, and
we can keep it on a simplest all the questions, everything
for now, I.
And design wise, we we have a go ahead Rajiv. We'll just start designing from today.
We go ahead to need here. Okay,
so it'll be like one week from when we start working on the design
question. I'm
understanding
so what I am
understanding that this may sections a copy, sorry, just a project. Okay. Volume, okay, right. So I believe there are a lot of screens on average of five in every section, right? So
volume, sentiment, drivers and
skin, the separate one one screen. What I thought was at least you can keep three different developers, and
if you can say integration, we can run independently pages.
Sorry, sorry to interrupt. I know I don't have any control over this, but can we, like, get someone like Shagun for this project I know for Palo Alto network, she, like, very painstakingly went through every single detail, and it was like,
Bucha clean.
I have no control over this, but I'm just saying
I have no problems. Panel, final word. Rajiv, okay,
because
contractual. Kamika Regina, she's not working with us anymore. Oh, okay,
so
cool. Bucha is available.
Quick project
she wants. She will join back if there is work,
okay, I think
last
year,
yeah, sure, so People and then Sakshat will be comfortable.
I'm just heating anyone will work. It was just
like confidence level. But that is much better,
good for us. No problem.
Questions.
Sakshat meeting, set up, and it may dominate in meaning,
total work here, yeah, two days,
method,
section, Roman,
so many already. Many already Sakshat for both the other but I need to take a closer,
and this is final right PC screen
to focus,
yep, from yesterday's conversation, Mark Mendel was saying that he has demos with some prospects,
demo that he hasn't shared. He just said, we have something in the books
and that we would like it as soon as possible.
But yeah,
he didn't think our deliverables will be somehow aligned with the demo.
See Sarah product
future, no dependent on their new prospect signing up or not.
Okay.
Prospecting,
yeah, Bucha, incremental, plan, banana, potato, key, okay, after three weeks, you will see the top navigation and at least few charts done integrated. Sa new about chart there among corporate integration,
they are very responsive. Bucha rogi, and you respond correctly.
Immediately, or what group people now? What? So,
although it's not Cisco, Style Me, company or guys miss me
over. Key outcome, base key, do we have something improved today that we can present in
Sakshat? Is that right? Is that you're also understanding? Yeah,
more or less Yes.
Sakshat ke sak, saktha, how to use and how to actually make a dashboard to do that.
Yes, also.
Raji, big, major concern.
Ah,
yes, yes.
Was,
I think, 13 February, 23
COVID front end both stronger, so I'll divide the task, and if, in case you stop, I'll do the front end of balance.
Okay,
take care.
Yeah,
take it. I'll continue with Sakshat, and persons plus
that so 30 day, remember, let them fit. Oh,
3045, minutes.
Yeah, take in the
meantime, take a Sakshat group. Hang out with discussion.
Yeah, let me know.
Yeah,
okay, I'll drop off for the next
answer.
Thank you.
Okay,
so from design point
of view,
no, not from a design point of view, from a design point of view, the way I see it, it's, it's more like,
it's more like urban planning, where I will basically set the guidelines for an entire city, and those guidelines will end up shaping, you know, smaller or larger parts of the city.
Okay, so that's how I would see it. It's I would see it something like this. Wait, I have this open somewhere.
No.
Yeah, so let me start this presentation.
So in DocuSign, what we had done is we had set up a basic anatomy like, okay, let's say these are your widgets. Within each widget, there are some guidelines on how these widgets will be built.
Your your screen is not shared. Oh, sorry. I
Okay, so now it's visible, yeah. So what we did was we set up some basic guidelines on how you know spacing will work for the entire platform.
This how it will be composed, like very specific locations for each object, and if you're talking about the widgets.
So actually, these are helpful for us from development what have you as well. Yeah, I'll be preparing stuff like this for for for ourselves. So yeah, I defined some basic guidelines on on what each element will be labeled. So like, tile, heading, localized filters, supporting metrics, database, legend, data table. So I would compartmentalize each of these aspects individually and set
I'll share some examples of how these can be built, like variations, but the basic idea would be centered around
like how those elements will be used, like when, when is the right time to use a drop down, when is the right time to use a slider?
How we can compose.
Pose each in certain situations,
specific spacing,
and yeah, and so it'll be like this. So the tile is designed to handle everything, whether it's a visualization or a table or a legend.
So I would basically just try to define guidelines for how this can be built.
So this can be considered as one widget, but at the same time, this tiny one can also be considered as one widget,
understood.
Okay, so these widgets, which you were showing me, these were only or displaying the data with respect to there was no internal operation on top of it, right in terms of what we were seeing right now, like solid bar coming in and all right? No, no, no. This is just a widget.
Still, it is helpful in terms of what you have built. I up. Actually,
I used to get similar kind of things when I was in my first
company, but, yeah, I think they were not following the same structure you front end. It's useful in terms of setting up the architecture for the front end code, visit to the CSS style guide and all that. So
I prepare these things and then some, then the people don't actually is useful. Yeah, actually it is useful. All the other designers should do this in our company. I don't know why they follow this. It is actually useful for us, and saves a lot of time at our end.
So, so, yeah, I'll be sharing these kinds of documents with them and you guys, so that will help you, you know, further streamline your time timeframe.
As far as how the demo, yeah, the demo, actually, there's not, there's not a lot to it, but I'll give you my overview of how I try to create this. For example, when I, when I made this sort of text box, I used a simple text widget.
It had enough customization capabilities to turn into this, like you can change text size, not a lot, but you can still change it. You can highlight text, make it bold italics, change font, things like that. The one thing you I couldn't do is I could copy text from somewhere else and paste it as it is here, Ctrl C, yeah, because individual screens are, that's what I said. And these are individual DOMs. I'm not sure that property is working fine. Let me take a look into the board. Yeah?
So, yeah, that was a big issue. Also, alignment was a major issue. Like, if I, if I try to edit this
now, I can't see the rest of the box. And if I work like this, I can't like, there's very little room for fine tuning or the esthetics aspect of it,
even if you, you know,
expand or collapse the screen. That whole thing will not be resulting in responsiveness of the not this one, the mother screen, the whole frame. Try to keep it, you know, expand or collapse the main screen. Can you try doing it?
So, yeah. So the internal, you know, frame, the elements within the internal frame, they will not
adjust according to that, yeah, because these internal elements are actually individual DOM elements.
So that is only applicable from that corner, you know, thing which you try to stretch it and all that stuff. So, yeah, get it when you're saying that. And I'm as far as, like, designing guidelines, just, yeah, just give us. Just give me one.
It.
Sorry, yeah, no problem. So
yeah, while setting guidelines for the canvas. So this gray area is what I'm calling the canvas. I'm actually thinking of just replicating some properties of other WordPress sites, because WordPress, for the most part, has already solved these kinds of problems of snapping.
Making sure the tiles are in columns. And if you want, you can immediately make it responsive.
So,
okay, okay, okay, got it. So you want another sort of a layer where you can fit all those tiles within, right? Yeah, and that, that act as a,
I need to think about it. That's why I asked
for the, you know, and you have already, that's what I was trying to understand, that whether this, this adjustment was done by you, or it was already adjusted the tires that you have played as of now, because at my end, I was just bringing everything.
It was not getting placed like this. It was just going here and there on the screen. No, it had to be composed so you read it by yourself, right? Yeah.
Everything had to be composed. But, but, yeah. The My idea was, these things, these principles around how a layout works, they're they're applicable in Tableau, most WordPress websites, and
I think to a degree, even in notion,
it can be done, but it depends, like,
what you know, what you are calling that Canvas thing, right? What exactly they are using for that as a tick. So I need to look and take a look into that. If you know on that Canvas library, whatever library they're using, if that is not allowing it to do so, we might need to change it. But I got your idea, like,
there will be a container kind of thing in which you want to place these tiles, and whatever will be the shape of the container accordingly, the individual
internal tiles will get adjusted, right? That's what you're Yeah, yeah, planning to do exactly something like that. So that way we can make sure, even if some
continuity, no, it will be responsive. That's all.
Ah, but the decoupage, I mean only what exactly they have done from there, yeah, if, if it is possible on the current one as well, I think it can be done if it allows to have a central container within that. So basically,
there will be another, you know, drag and drop thing on the left hand side. That will be the container again, and after that, whenever you are putting a tile on that Canvas, you need to put the tile in the container,
social property, just so the idea and subsequent tiles COVID Just within the container itself, be it length of bread, the whole size. And basically, you can move the individual tiles within the container and do the same sort of adjustment of layout what you have done right now, something like that. Something, once you stretch the whole container, the internal elements will also get stretched accordingly from length, exactly, yes, Google Sites again, that's a good example to play around with. So if
i Where is Google Slides? Oh, sorry, Google Sites, not slides.
I think I have used it, yeah, so we can essentially create
an experience like this.
No, I but yes, but that's what I want to hear.
I am understanding the structure over there, over there and there. So I
It's May or is my difference?
Yeah, but yeah, what you are trying to establish now, the only thing is, I need to see concurrent current implementation, yes, sir. Or with respect to time, it now time
and how easy or difficult it is on their current implementation. I like the idea, though, but where he I'll focus on the initial work first. I mean the other, you know, primary jobs, yeah, then we can jump on to that. But I like the idea problem in Mary. It
in Mary screen. It was going somewhere else in the screen, and the data was hidden the mujahi individually tiles, course text. And that was a painful job.
Yeah, I mean, I'm user going to go exactly so.
Okay, so that's another thing we can look into.
So I don't know if this counts as a concern, but there are small things like, I remember when I was trying to edit the title for this key movements, you know, typically how
we would select an entire text area like this and get highlighted. I can delete it and type whatever I want. That's not possible. Okay, just just one, this one. Sorry to interrupt. Can you try again, dragging it up, which you did, just like, Okay. And
in India,
you see what I'm talking about.
So you're saying it. These tiles can adjust themselves, but they haven't gone ahead and
they have not drawn the boundaries here. Okay,
maybe we can do it from our Yeah, you can continue. So with the text editing part, yeah, it's just painful to edit text. I can't actually select the whole thing.
I'll have to, if I need to rename the whole thing, I had to individually delete it like this and then
write another. So the whole select text is not able. You're not able to select. The whole text. Select all is not working.
Okay, this is another property. So the similar thing, it is related to that copy and paste somehow?
Yeah, yeah. So I need to see if they have disabled it.
We have a property to disable these kind of, you know, abilities, copying, pasting, moving and all that stuff. So I'll take a look into that. Yeah.
Another challenge I experienced was with these filters, I guess I'll just have to get accustomed to it first. Oh,
okay, okay, okay.
So remember,
in luminoso there's a concept called active concepts, which means you can basically create your own subset of keywords, topics, yeah. And my assumption was a user cannot create those subsets and then bring them into this,
this platform, but it looks like, Oh, yeah. It looks like they can,
they can. But how you know whatever subset you are making, how the you know data will get adjusted to that? Do we have any mechanism where we need to map the data with that particular subset? I don't know. Let's try. So if I select Helios themes,
what happens?
Okay,
so just basically re rendered the same chart, but with different concept words.
I think I was expecting that they have a set of this whole thing, lot of tapes, and, you know, they're building a relationship between that. As soon as you are entering another, you know, topic, based on that topic, it will search all those words and show it to YouTube.
No, they, they would, they have a predefined set of topics. And even in that predefined set of topics, there's, there's exact match, and there's conceptual match. So for example, in a Okay, okay, let's say they have 10,000 comments out of that. This the comments that have an exact match with the word excellent is probably this month, okay?
And then conceptually,
how many other comments have a match with the word Excellent. So that's this, like, in sense of meaning, in sense of meaning, right? Yeah. So it's like a synonym or similar.
So that's how they're doing it.
So from topic point, like, whatever they are calling it as concept that is for us, this topic right for us, it's it's like a keyword, or,
let me see if I can open one document.
Okay, takes a few seconds.
Okay, so this is one document.
Like, let's say a user has left this review
out of that.
How many times is customer mentioned? How many times is care mentioned? So these keywords turn as concepts.
Okay, so it's like, if, if I want to understand people's opinions on parking lots for grocery stores, then I will look at all the comments that are that have an exact match of parking lot and a conceptual match of parking lot,
like parking area or parking segment. That word could be a positive, negative, all that stuff, and based on that, we can have a sentiment score and see the negativity, or maybe in the with the combination. I think that's what they have shown in with respect to combination, whether it is positive or negative. What is the percentage of positivity and negativity? Yeah. So I think they they calculate sentiment here in some way. So all the comments that have the word issue, 80% have a negative sentiment, which is probably obvious.
Percent have a positive like, I had issues, and I'm not having issues positive, negative. Yeah.
Sakshat, did you work on Atlas earlier with us? No.
So it is similar to it's a very advanced but what I am saying is it is very advanced version of Atlas. So if you go
on the main dashboard,
scroll up and click on No, no, no. Okay,
that can go, click on,
okay, go back
where we are having list of all those companies, right.
List of,
oh, okay, okay, the previous screen, the previous No, no, no. Let me share my screen. Yeah. So
I don't know whether if Rajiv noticed this. I think this is what we were trying to do with Atlas. But a lot of challenges, challenges of the decision making. Main challenge I was talking about the screen, so when you click on new project now,
so there you need to, cannot this one. Actually, it was new data stream
from where we need to pick the data. So, yeah, already from where exactly we need to pick the data.
Upper we can basically put the URLs. So similar thing we are doing on this scrape or a specific company from different different sources, and once that data is completely scraped and it is in our databases,
basically, in our case, it it looks like This. Only word,
not that good, but was maybe eight. A, we prepare a sentiment chart, C, start score and all that stuff. Word Cloud, what words have appeared, how many times they have appeared?
This is how I see.
You're doing the same thing in Atlas, but not like this.
So I'm not sure whether aji noticed this not.
Probably worth a discussion,
though. I think he might have mentioned Atlas in with you earlier, maybe sometime earlier. Yeah, he's, he's mentioned Atlas. I wasn't, like, directly involved in it, but, but yeah, he's mentioned it. The only thing, the bigger difference, what I see is they, they have a lot of data sources that are there, and we only kept g2
then trust pilot, then maybe Google App Store and Play Store,
and that's it. We were having only these data sources and Gartner in capeha.
The only thing I don't understand is how they calculate NPS just from text.
Okay,
okay, I'll share the APIs, which we created for NPs and CSAT and all that stuff. What's simple? Then we have a library, Joe natural language in lower
NLP, use,
natural language processing given away library, use key, okay.
What they do is basically they check two things. One is basically the individual word. The individual word could be also having a positive or negative set meaning follow in terms of the whole thing, and then they see the combination that liberties check, the combination like that word attached with what other word, whether it is pre or post, worst case basis for sentiment, Nichols, that it is somewhere between a.
Minus five to plus five.
Again, the combination at all it is coming from where, whether it is this sentence that sentence, let's say 100 reviews. Are there, right? 200 reviews, basis for us, scan wherever pre defined.
And if, in case, just a CSR, also calculate, but your basic somehow, it is somehow coming with the sentiment part only to basic scoring individual words, but we basically have different different formulas for C start and all that stuff, which we need
to clarity. So at least if you just check, you can experiment
with that. But here I was basically working on Node in Logan, a python two. It was working very slow. Python
create agency. We recreated the whole stuff. They were scrapping the whole data,
let's say company, I mean upon sources, data, sources area. It was taking the whole day. I'm Logan again with Sarah data. Mushkil said, dominate.
So us may have me a Sara score, a key bar, which is a look Lord, he indicates maybe he's working. We were trying to create the project was making the URL, lady like I'm saying, very excited company, whiskey. Reviews, Amazon, pay her
Gartner, pay her trust. Pilot,
so many, sorry. URLs.
You look at the only he was Sarah. Data was Sara. Again, you understanding their
architecture.
So okay, that's how I'm understanding their architecture.
Got it
interesting.
It is interesting. I'm just I'm naturally a skeptic. So now I'm questioning that calculation on like, How does someone decide based on a sentence, like, I know it's set defined in the library, but how does someone actually define a number to things like this? Okay, I'll keep I'll make it more easy for you. Did you check this? How we work on this thing? How traditional llms work?
I mean, I understand conceptually, but yeah,
not more than that. Stuff is simple in key central database hobby, which will be a vector database, right? Vectors may basically, we are storing numbers. So you can see it in this way, like, let's say there is a sentence which is a meaningful sentence. Like, let's say if this, if that's if there is something like COVID sentence, this is a bottle, right? This is a bottle, right? So, vector database, what we do is we convert this whole sentence into tokens. Token, yeah, individual word which is making or digital bird, or a combination which is making some sense, right?
In COVID X, area and those numbers are somehow also related within themselves. Is number vector, many
vector databases sold now the whole vector database might have a whole number of vectors combinations,
right? So whenever you are taking just one word,
one you know, or a series of words with their which, which will be having their own number attached, right?
So what token is vector database? Right? Just does a search, right, and it gives you back the very matching combination which could be possible, right?
So this is how we, basically, you know, make some sense out of that.
That is a very basic thing which we do in this natural language processing. This is what they might be using. In fact, they will be using this only, not finally, they will be using this only, okay,
sounds interesting, but, yeah, interesting. Okay, what
I'll do now is I'll try to trans like, check the transcript of this meeting and break down all the questions that you have posed.
I'll send over those questions to you if you want. You can add more questions or edit those questions. But once we have that, I'll try to set up some meeting with with John,
yeah, try to, you know, remove all that extra content, which we discussed. I absolutely.
Totally, yeah, that's easy, yeah, okay, and what's the latest that you can stay up? Like,
latest as in, like, oh, early. I can share it. No, like, right now, at six o'clock. So okay, latest as in, like, what is, what will be the last time, like, in terms of my availability, right? Yeah,
my jala, availability.
Keep on working so you can adjust the, you know, meeting accordingly based on your availability as well. No problem in that.
Okay, at least max to max. Keep it before. Well, just so that I am not, you know, that time I'm not exhausted? Yeah, absolutely. I'll have energy. Yeah, I was thinking more like 10:10pm, would be the max, but, yeah, 12 is fairly reasonable. I'll try to keep it at 10 Max. That's beyond 10 or 1011, 30, okay,
because I need to prepare questions as well from iron, and we'll also give some time to them as well. My question, please do I'm planning art, which is my 8pm I can share the question so that they can get at least two or two and a half hours to, you know, read it from there.
What do you suggest?
I I have no problem with that. I think that's ideal. So
let me see. I'll, I'll also see if this transcript can, like, speed up the question generation thing. So if we have that, then I'll, as soon as we have the questions, I'll just set up, send it, no problem. Then he'll set up the Meeting.
Bye,
Okay, Bye, Bye.

## ChatGPT (2025-01-22T12:42:45.237697+00:00)

Here’s a detailed list of all the questions from the meeting that need to be clarified with the stakeholders:

---

### 1. Libraries and APIs
- **What libraries are they currently using?** Are there specific preferences or restrictions on libraries we can integrate?
- **Which specific APIs are being used for the dashboard?**
  - A list of all APIs involved in DAPP integration is required for front-end code development.
- **Is the API version listed as v5 accurate?** Are there any planned updates to this version?

### 2. AI Summaries and Widgets
- **How do AI summaries work across widgets?**
  - Currently, summaries exist only for select widgets. How will they scale to other widgets?
- **Is there a walkthrough or documentation on creating summaries for specific widgets (e.g., "Largest Concept Movement")?**
- **Can users customize summaries for individual widgets, or is it automated?**

### 3. Dashboard and Widget Behavior
- **How should we handle different visualizations for widgets?**
  - What level of customization is required (e.g., smooth vs. angular lines)?
- **What is the expected behavior for filters?**
  - How should local and global filters interact with charts and other visualizations?
- **How should text boxes (e.g., Text Widget) function?**
  - Are features like copy-paste, text alignment, and resizing requirements?

### 4. User Experience (UX)
- **Is there a need for an onboarding flow for the dashboard?**
  - If so, what key elements should the onboarding highlight?
- **Should we prepare templates or guidelines for users to structure their visualizations?**

### 5. Technical Considerations
- **Is the current codebase available for review?**
  - This is crucial to understand matching screens, completely different screens, and potential design/development efforts.
- **How do filters impact performance?**
  - For example, if multiple filters trigger simultaneous API calls, are there performance thresholds we should consider?
- **Can the current implementation support container-like layouts for responsive design?**
  - If not, are there suggestions for alternatives or modifications?

### 6. Concept and Data Integration
- **What is the process for creating or importing "Active Concepts"?**
  - Can users create custom subsets of keywords or concepts for integration into dashboards?
- **How do predefined concepts like "Customer" and "Care" map to comments or documents?**
- **How is sentiment (positive/negative) calculated for specific keywords or concepts?**
  - Are these calculations customizable?

### 7. Project Timeline and Scope
- **What are the most critical deliverables aligned with the demo?**
  - Are there specific widgets, screens, or functionalities required for the stakeholder demos?
- **What are the expectations for incremental deliverables (e.g., navigation, chart integration)?**
- **What is the priority for scalability across the rest of the application?**

### 8. Additional Team Support
- **Are additional resources (e.g., designers, developers) available for this project?**
  - If not, how can we adjust timelines or expectations to accommodate the limited capacity?

---

This summary focuses on the key points from the meeting. Let me know if I missed anything, and we can refine the list further.

## You (2025-01-22T12:43:37.642288+00:00)

could u read through all the pages in this website
https://daylight.luminoso.com/api/v5/

and let me know if this answers any of the questions we just discussed



## ChatGPT (2025-01-22T12:43:48.259673+00:00)

After reviewing the Luminoso Daylight API v5 documentation , here are the insights related to our previously discussed questions:

**1. Libraries and APIs**

- **API Version**: The documentation confirms that the current API version is v5. There is no mention of any planned updates beyond this version.

- **Available Endpoints**: The API provides various endpoints categorized under Projects, Documents, Terms, Concepts, Dashboards, and more. Each endpoint is documented with its functionality, required parameters, and expected responses.

**2. AI Summaries and Widgets**

- **Concept Sentiment**: The "Get concept sentiment" endpoint offers sentiment analysis at the concept level, providing sentiment share and raw counts for each concept. Notably, project-wide sentiment share and counts have been deprecated as of September 10, 2022, indicating a shift from document-level to concept-level sentiment analysis.

**3. Dashboard and Widget Behavior**

- **Dashboards Endpoint**: The API includes endpoints for managing dashboards, such as listing available dashboards, creating new ones, and retrieving dashboard data. However, specific details about widget customization, filter interactions, and text box functionalities are not elaborated in the provided documentation.

**4. User Experience (UX)**

- The documentation does not provide information regarding onboarding flows or user experience guidelines for the dashboard.

**5. Technical Considerations**

- **Rate Limits**: The API enforces a default rate limit of ten requests per second. Exceeding this limit results in a 429 error. Some endpoints may have different rate limits, which are specified in their respective documentation.

- **Deprecations**: Certain fields and parameters have been deprecated. For instance, the "skip_rebuild" parameter in the "Copy project" endpoint was deprecated on November 5, 2022, with its removal scheduled for April 25, 2023. It's essential to review the deprecations section to ensure compatibility.

**6. Concept and Data Integration**

- **Term Management**: The API provides endpoints for retrieving and updating term management information, which can be useful for handling concepts and their associations.

**7. Project Timeline and Scope**

- The documentation does not specify details about project timelines, deliverables, or scalability considerations.

**8. Additional Team Support**

- Information regarding team resources or support is not covered in the API documentation.

**Conclusion**

While the Luminoso Daylight API v5 documentation offers valuable technical details about available endpoints, functionalities, and certain limitations, it does not comprehensively address all our previously discussed questions, especially those related to user experience, widget behavior, and project-specific considerations. For those areas, direct communication with the stakeholders would be more effective.

## You (2025-01-22T12:45:58.315977+00:00)

ok, now could you review our meeting transcript one more time to identify all the questions that we need to clarify from the stakeholders, give me the answers (and if no answer is available, point it out, and create some follow up questions based on the existing answers that a front end team might need to know before giving any estimate on the amount of work,  timelines, and any additional complexities in the project

## ChatGPT (2025-01-22T12:46:56.654714+00:00)

### Review of Meeting Transcript: Questions, Answers, and Follow-ups

Here’s a breakdown of the questions from the meeting, answers (if available), and follow-up questions that the front-end team might need clarification on before providing an estimate on work, timelines, and complexities.

---

### **1. Libraries and APIs**
#### Questions:
- **What libraries are they currently using?**
  - **Answer:** No information provided. Needs clarification.
  - **Follow-up:** Are there preferred or restricted libraries for charting, visualization, or front-end frameworks?

- **Which APIs are being used for the dashboard?**
  - **Answer:** The Luminoso Daylight API v5 is the confirmed version. Details about API endpoints for dashboards and concepts are available.
  - **Follow-up:**
    - Are there specific endpoints for visualizations and filters that should be prioritized?
    - Do the APIs support real-time data fetching and updates, or is it a batch process?

- **What is the expected interaction between the APIs and front-end components?**
  - **Answer:** The APIs seem to provide data for concepts, sentiment, and dashboards, but specifics on interaction patterns are unclear.
  - **Follow-up:**
    - How will API rate limits impact the front-end performance (e.g., 10 requests/sec)?
    - Will there be any APIs specifically for managing custom widgets?

---

### **2. AI Summaries and Widgets**
#### Questions:
- **How do AI summaries work across widgets?**
  - **Answer:** AI summaries currently exist for select widgets, summarizing concepts like "largest concept movement."
  - **Follow-up:**
    - Will summaries automatically generate for all widgets, or will there be a user-triggered action?
    - Are there customization options for AI summaries?

- **How will widgets like “Volume over Time” and “Sentiment over Time” handle API inputs?**
  - **Answer:** Each widget appears to interact with individual APIs but further clarity is needed.
  - **Follow-up:**
    - Are there specific APIs tied to each type of widget, or will there be shared endpoints?
    - Can multiple widgets request data simultaneously without performance degradation?

---

### **3. Dashboard and Widget Behavior**
#### Questions:
- **What level of customization is required for widgets?**
  - **Answer:** Users should be able to customize visualizations (e.g., bar charts, line charts, filters). Details on text box customization are unclear.
  - **Follow-up:**
    - Should all widgets support advanced styling, such as smooth/angular lines or custom colors?
    - Is there a need for drag-and-drop reordering of widgets?

- **How should filters (local and global) interact with visualizations?**
  - **Answer:** Filters impact both local widgets and global data views.
  - **Follow-up:**
    - How will filters be structured (hierarchical or flat)?
    - Should changes in one widget's filter affect others, and if so, how?

---

### **4. User Experience (UX)**
#### Questions:
- **Is there a need for onboarding flows or help systems?**
  - **Answer:** Stakeholders seem to support the idea, but time constraints make this unclear.
  - **Follow-up:**
    - Should onboarding include interactive tutorials or tooltips?
    - Are there plans to include templates or pre-built dashboards for new users?

- **What are the guidelines for responsive design?**
  - **Answer:** Front-end elements like containers and tiles should adjust to the screen size.
  - **Follow-up:**
    - Should all widgets dynamically adjust, or will fixed layouts be acceptable?
    - Are there restrictions on library choices for handling responsiveness?

---

### **5. Technical Considerations**
#### Questions:
- **What is the codebase structure?**
  - **Answer:** Codebase access is required to determine the relationship between widgets and screens.
  - **Follow-up:**
    - Are widgets modular or tightly integrated into the dashboard?
    - How many unique screens will require separate layouts or functionality?

- **What are the scalability requirements?**
  - **Answer:** No detailed information provided.
  - **Follow-up:**
    - Are there plans to scale dashboards to handle larger datasets or additional users?
    - Should designs account for multi-language support or accessibility standards?

- **What are the performance benchmarks?**
  - **Answer:** Filter interactions may trigger multiple API calls, potentially causing delays.
  - **Follow-up:**
    - Is there an expected performance threshold for API response times?
    - Should we implement lazy loading or caching mechanisms to improve performance?

---

### **6. Concept and Data Integration**
#### Questions:
- **How will active concepts and subsets be used?**
  - **Answer:** Users can create subsets of keywords and concepts, but the integration mechanism is unclear.
  - **Follow-up:**
    - Can subsets be saved and reused across dashboards?
    - Are there APIs to create and manage subsets directly from the UI?

- **How is sentiment calculated and displayed?**
  - **Answer:** Sentiment analysis is available for concepts, but exact calculations are unclear.
  - **Follow-up:**
    - Are there predefined thresholds or categories for sentiment (e.g., positive, negative, neutral)?
    - Can sentiment values be overridden or customized?

---

### **7. Project Timeline and Scope**
#### Questions:
- **What are the critical deliverables for the stakeholder demo?**
  - **Answer:** Charts and navigation are high priorities.
  - **Follow-up:**
    - Are there specific widgets or functionalities that must be completed for the demo?
    - Is there a preference for demonstrating breadth (more features) or depth (fully functional components)?

- **What are the long-term scalability goals?**
  - **Answer:** No specific information provided.
  - **Follow-up:**
    - Will future iterations require cross-platform compatibility (e.g., mobile apps)?
    - Should we prioritize modularity for easier updates?

---

### **8. Additional Team Support**
#### Questions:
- **Are additional team members or resources available?**
  - **Answer:** No additional resources were confirmed.
  - **Follow-up:**
    - If the timeline is tight, are there external consultants or temporary hires available?
    - Can tasks be prioritized to align with the existing team's capacity?

---

### Summary

- **Questions Needing Answers:**
  Most questions about libraries, customization, data integration, and scalability remain open.

- **Follow-up Questions for the Front-End Team:**
  Focus areas include API interaction details, modularity of widgets, and performance benchmarks.

Would you like me to compile this into a document or further prioritize these questions for an immediate stakeholder review?
