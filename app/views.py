from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def home(request):
    context = {"title":"Home - AlgoHub"}
    return render(request,template_name="pages/home.html",context=context)

@api_view(['GET'])
def start_page(request):
    context = {"title":"AlgoHub"}
    return render(request,template_name="pages/start_page.html",context=context)

@api_view(['POST'])
def analyze_code(request):
    # <div class='flex w-full'>
    #         <div class='flex flex-col space-y-4 items-start space-y-3 w-full space-y-4'>
    #             <div class='flex justify-between items-center w-full'>
    #                 <p class='text-1xl font-bold'>Graph</p>
    #                 <button class='w-[13rem] mx-1 bg-blue-400 rounded-lg text-white px-6 py-2 cursor-pointer'>Dowbload Report</button>
    #             </div>

    #             <div class="graph-wrapper">
    #             </div>
    #             <p class='text-1xl font-bold'>Summary and Suggestions</p>
    #             <div>
    #                 <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Rem sunt dolores veritatis architecto, fuga voluptas?</p>
    #                 <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quam illo in ut enim iure explicabo deserunt dolorem, odit maxime, vel consequuntur. Eaque ea laboriosam sequi.</p>
    #                 <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sit voluptate ut nam deserunt dignissimos temporibus, beatae voluptatem tempore! Voluptatem, adipisci! Hic delectus ipsam nobis nihil aliquam voluptas sapiente saepe, repellat distinctio. Hic dolores repudiandae at aliquid eum temporibus mollitia iusto numquam cumque? Nihil totam commodi incidunt, consectetur earum exercitationem distinctio.</p>
    #             </div>
    #         </div>
    #     </div>
    #             <div class='flex justify-between items-center w-full'>
    #                 <p class='text-1xl font-bold'>Graph</p>
    data = {"code":"<div class='flex flex-col space-y-4 items-start space-y-3 w-full space-y-4'><div class='flex justify-between items-center w-full'><p class='text-1xl font-bold'>Graph</p><button class='w-[13rem] mx-1 bg-blue-400 rounded-lg text-white px-6 py-2 cursor-pointer'>Dowbload Report</button></div><div class='graph-wrapper'><img src='{% static 'images/graph.jpeg' %}' alt=''></div> <p class='text-1xl font-bold'>Summary and Suggestions</p><div><p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Rem sunt dolores veritatis architecto, fuga voluptas?</p><p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quam illo in ut enim iure explicabo deserunt dolorem, odit maxime, vel consequuntur. Eaque ea laboriosam sequi.</p><p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sit voluptate ut nam deserunt dignissimos temporibus, beatae voluptatem tempore! Voluptatem, adipisci! Hic delectus ipsam nobis nihil aliquam voluptas sapiente saepe, repellat distinctio. Hic dolores repudiandae at aliquid eum temporibus mollitia iusto numquam cumque? Nihil totam commodi incidunt, consectetur earum exercitationem distinctio.</p></div></div>"}
    return Response({"success":True,"data":data},status=status.HTTP_200_OK)
# Create your views here.
